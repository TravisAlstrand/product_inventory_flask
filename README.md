# S.M.E.A.G.O.L

## What is it?

This was originally a blend of Team Treehouse's Python TechDegree's projects 4 and 5 and Data Analysis' project 4. It's a Lord of the Rings themed Python, Flask-SQLAlchemy project where you can perform crud operations on fictional products and brands stored in a SQLite3 database.

The database is populated from reading a CSV file on start-up if the database is not already populated.

It uses vanilla CSS and JavaScript for front-end visualization and interactivity.

## Installation

- Download or clone the GitHub repo
- Open your terminal and create an environment
  - `python3 -m venv env`
- Activate the environment
  - `source ./env/bin/activate`
- Install dependencies
  - `pip install -r requirements.txt`
- Start app
  - `python app.py`
- Open `http://localhost:3000` in your browser

## Usage

If you make too many edits and want to refresh the database...

- Stop the app in the terminal
  - `CTRL + C`
- Delete the database
  - `rm instance/products.db`
- Restart app
  - `python app.py`

If you create a new Brand or Product and want a picture associated with it, add the image to the respective folder in the `/static/images/` directory. Ensure the name of the file is the exact Brand or Product name with `-` hyphens instead of spaces and a `.jpg` extension. For example, the product "Best Product" should be saved in/as `/static/images/product-images/Best-Product.jpg`.

## Credits

All Brand and Product names and descriptions were created by Chat-GPT and all images, logos and borders were created with Dall-E (because ain't nobody got time for that!).

Project uses the following fonts from [DaFont](https://www.dafont.com/)...

- [Bilbo Hand](https://www.dafont.com/bilbo-hand.font)
- [Hobbiton](https://www.dafont.com/hobbiton.font)
- [RingBearer](https://www.dafont.com/ringbearer.font)
