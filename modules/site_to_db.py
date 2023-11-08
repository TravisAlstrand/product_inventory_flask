import datetime
from modules.handle_search import get_single_brand, get_single_product, handle_search
from modules.models import db, Product, Brand


def updateBrand(original, new_name):
  brand = get_single_brand(original)
  if brand:
    new_name_already_exists = handle_search("Brands", new_name.lower())
    if len(new_name_already_exists) == 0:
      brand.brand_name = new_name
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
  if product:
    new_name_already_exists = handle_search("Products", new_name.lower())
    if len(new_name_already_exists) == 0:
      product.product_name = new_name
      product.product_price = form_data["product_price"]
      product.product_quantity = form_data["product_quantity"]
      product.date_updated = datetime.date.today()
      db.session.commit()
      return "success"
    else:
      return f"There is already a Product with the name {new_name}, try again!"
  else:
    return "Sorry there was an error!"


def create_new(category, form_data):
  print(category)
  print(form_data)