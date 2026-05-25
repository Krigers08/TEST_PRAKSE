import os
from app import app, db, Product

mysql_user = os.getenv("MYSQLUSER", "root")
mysql_password = os.getenv("MYSQLPASSWORD", "")
mysql_host = os.getenv("MYSQLHOST", "localhost")
mysql_port = os.getenv("MYSQLPORT", "3306")
mysql_db = os.getenv("MYSQL_DB", "store")

if mysql_password:
    db_url = f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}"
else:
    db_url = f"mysql+pymysql://{mysql_user}@{mysql_host}:{mysql_port}/{mysql_db}"

app.config["SQLALCHEMY_DATABASE_URI"] = db_url

with app.app_context():
    db.create_all()

    # Clear existing products
    Product.query.delete()

    # Add sample products
    products = [
        Product(name="Widget", price=9.99, description="A useful widget"),
        Product(name="Gadget", price=19.99, description="A handy gadget"),
        Product(name="Tool", price=14.99, description="An essential tool"),
        Product(name="Device", price=29.99, description="A cool device"),
    ]

    for product in products:
        db.session.add(product)

    db.session.commit()
    print("✅ Database seeded with 4 products!")
