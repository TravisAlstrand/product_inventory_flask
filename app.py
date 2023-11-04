from flask import render_template, request, redirect, url_for
from os.path import exists
from modules.models import db, app
from modules.csv_to_db import add_csv_to_db
from modules.handle_search import handle_search, get_single_product, get_single_brand


# HOME
@app.route("/")
def index():
  return render_template("index.html")


# GET STARTED
@app.route("/get-started", methods=["GET", "POST"])
def get_started():
  if request.form:
    print(request.form["b_or_p"])
    print(request.form["category"])
    if request.form["category"] == "search":
      return redirect(url_for("search_page", category=request.form["b_or_p"]))
  return render_template("get-started.html")


# SEARCH PAGE
@app.route("/search/<category>", methods=["GET", "POST"])
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
  brand_count = get_single_brand(result)
  return render_template("brand-detail.html", brand=brand_count[0], count=brand_count[1])


# EDIT PAGE
@app.route("/<category>/edit/<item>", methods=["GET", "POST"])
def edit_page(category, item):
  if request.form and category == "brand":
    print(request.form["brand_name"])
    return redirect(url_for("brand_detail", result=item))
  elif request.form and category == "product":
    print(request.form["product_name"])
    print(request.form["product_price"])
    print(request.form["product_quantity"])
    return redirect(url_for("product_detail", result=item))
  if category == "brand":
    item = get_single_brand(item)
    return render_template("edit.html", category=category, item=item[0])
  else:
    item = get_single_product(item)
    return render_template("edit.html", category=category, item=item)

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
  