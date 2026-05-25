import os
from app import app, db, Product

database_url = os.getenv("DATABASE_URL") or "sqlite:///store.db"
app.config["SQLALCHEMY_DATABASE_URI"] = database_url

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
