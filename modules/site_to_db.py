import datetime
from modules.handle_search import get_single_brand
from modules.models import db, Product, Brand

def updateBrand(original, new_name):
  brand = get_single_brand(original)
  if brand:
    new_name_already_exists = get_single_brand(new_name)
    if new_name_already_exists is None or brand.brand_name == new_name:
      brand.brand_name = new_name
      brand.date_updated = datetime.date.today()
      db.session.commit()
      return "success"
    else:
      return f"There is already a Brand with the name {new_name}, try again!"
  else:
    return "Sorry there was an error!"
