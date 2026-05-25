import os
from app import app, db, Product

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

with app.app_context():
    db.create_all()
    Product.query.delete()

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
