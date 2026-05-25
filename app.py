from flask import Flask, render_template

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Widget", "price": 9.99, "description": "A useful widget"},
    {"id": 2, "name": "Gadget", "price": 19.99, "description": "A handy gadget"},
    {"id": 3, "name": "Tool", "price": 14.99, "description": "An essential tool"},
    {"id": 4, "name": "Device", "price": 29.99, "description": "A cool device"},
]

@app.route("/")
def store():
    total = sum(p["price"] for p in PRODUCTS)
    return render_template("store.html", products=PRODUCTS, total=total)

@app.route("/product/<int:product_id>")
def product(product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    return render_template("product.html", product=product) if product else "Not found", 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
