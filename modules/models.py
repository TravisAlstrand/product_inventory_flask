from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="../static", template_folder="../templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
db = SQLAlchemy(app)

class Brand(db.Model):
  __tablename__ = "brands"

  brand_id = db.Column(db.Integer, primary_key=True)
  brand_name = db.Column(db.String())
  brand_description = db.Column(db.Text())
  products = db.relationship("Product", back_populates="brand", cascade="all, delete, delete-orphan")


class Product(db.Model):
  __tablename__ = "products"

  product_id = db.Column(db.Integer, primary_key=True)
  product_name = db.Column(db.String())
  product_price = db.Column(db.Integer)
  product_quantity = db.Column(db.Integer)
  date_updated = db.Column(db.Date)
  product_description = db.Column(db.Text())
  brand_id = db.Column(db.Integer, db.ForeignKey("brands.brand_id"))
  brand = db.relationship("Brand", back_populates="products")