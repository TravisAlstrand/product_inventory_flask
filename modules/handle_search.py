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


def check_if_exists(table, query):
  results = []

  if table == "Products":
    table = Product
  elif table == "Brands":
    table = Brand

  for item in db.session.query(table):
    if table == Product:
      if query == item.product_name.lower():
        results.append(item)
    else:
      if query == item.brand_name.lower():
        results.append(item)
  return results


def get_single_product(name):
  return db.session.query(Product).filter(Product.product_name == name).one_or_none()


def get_single_brand(name):
  return db.session.query(Brand).filter(Brand.brand_name == name).one_or_none()


def get_brand_product_count(name):
  brand = db.session.query(Brand).filter(Brand.brand_name == name).one_or_none()
  if brand:
    count = db.session.query(Product).filter(Product.brand_id == brand.brand_id).all()
    return len(count)


def get_all_brands():
  all_brands = []
  for item in db.session.query(Brand):
    all_brands.append(item)
  return all_brands
