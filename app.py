from flask import render_template#, url_for, request, redirect
from os.path import exists
from modules.models import db, app
from modules.csv_to_db import add_csv_to_db


# HOME
@app.route("/")
def index():
  return render_template("index.html")

# PRODUCTS
@app.route("/browse-products")
def browse_products():
  return render_template("browse-prods.html")

@app.route("/search-products")
def search_products():
  return render_template("search-prods.html")

@app.route("/add-product")
def add_product():
  return render_template("add-prod.html")

# BRANDS
@app.route("/browse-brands")
def browse_brands():
  return render_template("browse-brands.html")

@app.route("/search-brands")
def search_brands():
  return render_template("search-brands.html")

@app.route("/add-brand")
def add_brand():
  return render_template("add-brand.html")

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
  