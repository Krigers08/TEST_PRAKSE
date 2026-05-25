import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Use MySQL if on Railway, SQLite for local dev
if os.getenv("MYSQLHOST"):
    mysql_user = os.getenv("MYSQLUSER")
    mysql_password = os.getenv("MYSQLPASSWORD")
    mysql_host = os.getenv("MYSQLHOST")
    mysql_port = os.getenv("MYSQLPORT", "3306")
    mysql_db = os.getenv("MYSQL_DB", "store")
    db_url = f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}"
else:
    db_url = "sqlite:///store.db"

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))

@app.route("/")
def store():
    products = Product.query.all()
    total = sum(p.price for p in products)
    return render_template("store.html", products=products, total=total)

@app.route("/product/<int:product_id>")
def product(product_id):
    product = Product.query.get(product_id)
    return render_template("product.html", product=product) if product else "Not found", 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
