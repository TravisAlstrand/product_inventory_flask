from flask import render_template, request, redirect, url_for
from os.path import exists
from modules.models import db, app
from modules.csv_to_db import add_csv_to_db
from modules.handle_search import handle_search, get_single_product, get_single_brand, get_brand_product_count, get_all_brands
from modules.site_to_db import updateBrand, updateProduct, create_new

# HOME
@app.route("/")
def index():
  return render_template("index.html")


# GET STARTED
@app.route("/get-started", methods=["GET", "POST"])
def get_started():
  if request.form:
    if request.form["category"] == "search":
      return redirect(url_for("search_page", category=request.form["b_or_p"]))
    elif request.form["category"] == "create":
      return redirect(url_for("create_new_page", category=request.form["b_or_p"]))
  return render_template("get-started.html")


# SEARCH PAGE
@app.route("/<category>/search", methods=["GET", "POST"])
def search_page(category=None, results=None):
  search_query = None
  if request.form:
    search_query = request.form["search"]
    results = handle_search(category.capitalize(), search_query.lower())
  return render_template("search.html", category=category, query=search_query, results=results)


# PRODUCT DETAIL PAGE
@app.route("/product/<result>")
def product_detail(result):
  result = get_single_product(result)
  return render_template("prod-detail.html", product=result)


# BRAND DETAIL PAGE
@app.route("/brand/<result>")
def brand_detail(result):
  brand = get_single_brand(result)
  count = get_brand_product_count(result)
  return render_template("brand-detail.html", brand=brand, count=count)


# EDIT PAGE
@app.route("/<category>/edit/<item>", methods=["GET", "POST"])
def edit_page(category, item):
  # IF SUBMITTING EDITS
  if request.form and category == "brand":
    brand_edit_message = updateBrand(item, request.form["brand_name"])
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
  

# CREATE NEW PAGE
@app.route("/<category>/create-new", methods=["GET", "POST"])
def create_new_page(category):

  new_cat = category.replace("s", "")
  if request.form:
    new_item_message = create_new(new_cat, request.form)
    if new_item_message == "success":
      return redirect(url_for(f"{new_cat}_detail", result=request.form[f"{new_cat}_name"]))
    else:
      return redirect(url_for("dupe_new_error_page", category=category, new_name=request.form[f"{new_cat}_name"]))

  all_brands = get_all_brands()
  return render_template("create-new.html", category=new_cat, brands=all_brands)

  
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
  db_exists = exists("./instance/projects.db")
  if db_exists is False:
    with app.app_context():
      db.create_all()
      # clean CSVs & add to db
      add_csv_to_db()
      
  app.run(debug=True, port=3000, host='127.0.0.1')
  