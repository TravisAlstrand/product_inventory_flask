from flask import render_template, request, redirect, url_for
from os.path import exists
from modules.models import db, app
from modules.csv_to_db import add_csv_to_db
from modules.handle_search import (handle_search, get_single_product, get_single_brand,
                                   get_brand_product_count, get_all_brands, get_all_products)
from modules.site_to_db import updateBrand, updateProduct, create_new

# HOME
@app.route("/")
def index():
  return render_template("index.html")


# CATEGORY SELECT
@app.route("/<activity>/category-select")
def category_select(activity):
  return render_template("category-select.html", activity=activity)

# BROWSE PAGE
@app.route("/<category>/browse-all")
def browse_page(category):
  if category == "brand":
    items = get_all_brands()
  else:
    items = get_all_products()
  return render_template("browse.html", category=category, items=items)


# SEARCH PAGE
@app.route("/<category>/search", methods=["GET", "POST"])
def search_page(category=None, results=None):
  search_query = None
  if request.form:
    search_query = request.form["search"]
    results = handle_search(category, search_query.lower())
  return render_template("search.html", category=category, query=search_query, results=results)


# CREATE NEW PAGE
@app.route("/<category>/create-new", methods=["GET", "POST"])
def create_new_page(category):
  if request.form:
    new_item_message = create_new(category, request.form)
    if new_item_message == "success":
      return redirect(url_for(f"{category}_detail", result=request.form[f"{category}_name"]))
    else:
      return redirect(url_for("dupe_new_error_page", category=category, new_name=request.form[f"{category}_name"]))
  all_brands = get_all_brands()
  return render_template("create-new.html", category=category, brands=all_brands)


# PRODUCT DETAIL PAGE
@app.route("/product/detail/<result>")
def product_detail(result):
  result = get_single_product(result)
  img_name = result.product_name.replace(" ", "-")
  has_img = exists(f"./static/images/product-images/{img_name}.jpg")
  return render_template("prod-detail.html", product=result, has_img=has_img, img_name=img_name)


# BRAND DETAIL PAGE
@app.route("/brand/detail/<result>")
def brand_detail(result):
  brand = get_single_brand(result)
  count = get_brand_product_count(result)
  img_name = brand.brand_name.replace(" ", "-")
  has_img = exists(f"./static/images/brand-logos/{img_name}.jpg")
  return render_template("brand-detail.html", brand=brand, count=count, has_img=has_img, img_name=img_name)


# EDIT PAGE
@app.route("/<category>/edit/<item>", methods=["GET", "POST"])
def edit_page(category, item):
  # IF SUBMITTING EDITS
  if request.form and category == "brand":
    brand_edit_message = updateBrand(item, request.form)
    if brand_edit_message == "success":
      return redirect(url_for("brand_detail", result=request.form["brand_name"]))
    else:
      return redirect(url_for('duplicate_error_page', category=category, item=item, new_name=request.form["brand_name"]))
  elif request.form and category == "product":
    product_edit_message = updateProduct(item, request.form)
    if product_edit_message == "success":
      return redirect(url_for("product_detail", result=request.form["product_name"]))
    else:
      return redirect(url_for('duplicate_error_page', category=category, item=item, new_name=request.form["product_name"]))
  # IF REQUESTING PAGE
  if category == "brand":
    item = get_single_brand(item)
    return render_template("edit.html", category=category, item=item)
  else:
    item = get_single_product(item)
    all_brands = get_all_brands()
    return render_template("edit.html", category=category, item=item, brands=all_brands)


# ALREADY EXISTS ERROR PAGE EDIT
@app.route("/error/<category>/<item>/<new_name>")
def duplicate_error_page(category, item, new_name):
  return render_template("dupe-error.html", category=category, item=item, new_name=new_name)


# ALREADY EXISTS ERROR PAGE NEW
@app.route("/error/<category>/<new_name>")
def dupe_new_error_page(category, new_name):
  plural = f"{category}s"
  return render_template("new-dupe-error.html", cat_single=category, cat_plural=plural, name=new_name)


# 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == "__main__":
  db_exists = exists("./instance/products.db")
  if db_exists is False:
    with app.app_context():
      db.create_all()
      # clean CSVs & add to db
      add_csv_to_db()
      
  app.run(debug=True, port=3000, host='127.0.0.1')
  