from modules.models import db, Product, Brand


def handle_search(table, query):
  results = []

  if table == "Products":
    table = Product
  elif table == "Brands":
    table = Brand

  for item in db.session.query(table):
    if table == Product:
      if query in item.product_name.lower():
        results.append(item)
    else:
      if query in item.brand_name.lower():
        results.append(item)
  return results


def get_single_product(name):
    return db.session.query(Product).filter(Product.product_name == name).one_or_none()

def get_single_brand(name):
    brand = db.session.query(Brand).filter(Brand.brand_name == name).one_or_none()
    print(brand.brand_id)
    if brand:
      count = db.session.query(Product).filter(Product.brand_id == brand.brand_id).all()
    return [brand, len(count)]
