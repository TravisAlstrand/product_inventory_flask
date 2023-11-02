from flask import render_template#, url_for, request, redirect
from os.path import exists
from modules.models import db, app
from modules.csv_to_db import add_csv_to_db


# HOME
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-started")
def get_started():
  return render_template("get-started.html")

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
  