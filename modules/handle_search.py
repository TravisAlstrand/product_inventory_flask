from modules.models import db, Product, Brand


def handle_search(table, query):
  table = get_table(table)
  results = []

  for item in db.session.query(table):
    if table == Product:
      if query in item.product_name.lower():
        results.append(item)
    else:
      if query in item.brand_name.lower():
        results.append(item)
  return results


def get_table(string):
    if string == "Products":
      return Product
    elif string == "Brands":
      return Brand