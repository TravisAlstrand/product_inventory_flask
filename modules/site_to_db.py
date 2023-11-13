import datetime
from modules.handle_search import get_single_brand, get_single_product, check_if_exists
from modules.models import db, Product, Brand


def updateBrand(original, form_data):
  brand = get_single_brand(original)
  og_name = brand.brand_name.lower()
  new_name = form_data["brand_name"]
  if brand:
    new_name_already_exists = check_if_exists("brand", new_name.lower())
    if len(new_name_already_exists) == 0 or og_name == new_name.lower():
      brand.brand_name = new_name
      brand.brand_description = form_data["brand_description"]
      brand.date_updated = datetime.date.today()
      db.session.commit()
      return "success"
    else:
      return f"There is already a Brand with the name {new_name}, try again!"
  else:
    return "Sorry there was an error!"
  

def updateProduct(original, form_data):
  new_name = form_data["product_name"]
  product = get_single_product(original)
  og_name = product.product_name.lower()
  if product:
    new_name_already_exists = check_if_exists("product", new_name.lower())
    if len(new_name_already_exists) == 0 or new_name.lower() == og_name:
      new_brand = get_single_brand(form_data["brand_name"])
      product.product_name = new_name
      product.product_price = form_data["product_price"]
      product.product_quantity = form_data["product_quantity"]
      product.product_description = form_data["product_description"]
      product.date_updated = datetime.date.today()
      product.brand = new_brand
      db.session.commit()
      return "success"
    else:
      return f"There is already a Product with the name {new_name}, try again!"
  else:
    return "Sorry there was an error!"


def create_new(category, form_data):
  if category == "brand":
    brand_already_exists = check_if_exists("brand", form_data["brand_name"].lower())
    if len(brand_already_exists) == 0:
      new_brand = Brand(brand_name = form_data["brand_name"], brand_description=form_data["brand_description"])
      db.session.add(new_brand)
      db.session.commit()
      return "success"
    else:
      return f"There is already a Brand with the name {form_data['brand_name']}, try again!"
  else:
    product_already_exists = check_if_exists("product", form_data["product_name"].lower())
    if len(product_already_exists) == 0:
      new_brand = get_single_brand(form_data["brand_name"])
      new_brand_id = new_brand.brand_id
      new_product = Product(product_name=form_data["product_name"], product_price=form_data["product_price"],
                            product_quantity=form_data["product_quantity"], date_updated=datetime.date.today(),
                            product_description=form_data["product_description"], brand_id=new_brand_id)
      db.session.add(new_product)
      db.session.commit()
      return "success"
    else:
      return f"There is already a Product with the name {form_data['product_name']}, try again!"


def delete_item(category, item_name):
  if category == "brand":
    brand = get_single_brand(item_name)
    if brand:
      db.session.delete(brand)
      db.session.commit()
      return "success"
    else:
      return "error"
  else:
    product = get_single_product(item_name)
    if product:
      db.session.delete(product)
      db.session.commit()
      return "success"
    else:
      return "error"
