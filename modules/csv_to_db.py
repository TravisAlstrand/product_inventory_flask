from modules.models import db, Brand, Product
import csv
import datetime

# open & read csv files and clean the data then add data to db
def add_csv_to_db():
  with open("./csvs/brands.csv") as csv_brands:
    brand_data = csv.reader(csv_brands)
    # skip header line
    next(brand_data)
    for row in brand_data:
      # check if brand is already in db
      brand_is_in_db = db.session.query(Brand).filter(Brand.brand_name == row[0]).one_or_none()
      if brand_is_in_db is None:
        # if not in db, add it to db
        name = Brand(brand_name=row[0], brand_description=row[1])
        db.session.add(name)
        db.session.commit()
      else: 
        pass

  with open("./csvs/inventory.csv") as csv_inventory:
    inv_data = csv.reader(csv_inventory)
    next(inv_data)
    for row in inv_data:
      product_is_in_db = db.session.query(Product).filter(Product.product_name == row[0]).one_or_none()
      if product_is_in_db is None:
        build_new_product(row)
      else:
        # if in db, compare dates for newest
        if product_is_in_db.date_updated < clean_csv_date(row[3]):
          db.session.delete(product_is_in_db)
          build_new_product(row)
        else:
          pass
    db.session.commit()


def build_new_product(row):
  name = row[0]
  price = clean_csv_price(row[1])
  quantity = clean_csv_quantity(row[2])
  date = clean_csv_date(row[3])
  description = row[5]
  brand_id = db.session.query(Brand).filter(Brand.brand_name == row[4]).first().brand_id
  new_product = Product(product_name=name, product_price=price,
                        product_quantity=quantity, date_updated=date,
                        product_description=description, brand_id=brand_id)
  db.session.add(new_product)


def clean_csv_price(price_str):
  new_str = price_str.replace("$", "")
  price_float = float(new_str)
  return int(price_float * 100)


def clean_csv_quantity(quantity_str):
  return int(quantity_str)


def clean_csv_date(date_str):
  split_str = date_str.split("/")
  month = int(split_str[0])
  day = int(split_str[1])
  year = int(split_str[2])
  return datetime.date(year, month, day)