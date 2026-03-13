from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 600}
]

# -------------------------------
# READ (GET all products)
# -------------------------------


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


# -------------------------------
# READ (GET one product)
# -------------------------------
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):

    product = next((p for p in products if p["id"] == product_id), None)

    if product:
        return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


# -------------------------------
# CREATE (POST new product)
# -------------------------------
@app.route("/products", methods=["POST"])
def create_product():

    data = request.get_json()

    new_product = {
        "id": len(products) + 1,
        "name": data.get("name"),
        "price": data.get("price")
    }

    products.append(new_product)

    return jsonify(new_product), 201


# -------------------------------
# UPDATE (PATCH product)
# -------------------------------
@app.route("/products/<int:product_id>", methods=["PATCH"])
def update_product(product_id):

    data = request.get_json()

    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    if "name" in data:
        product["name"] = data["name"]

    if "price" in data:
        product["price"] = data["price"]

    return jsonify(product)


# -------------------------------
# DELETE product
# -------------------------------
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):

    global products

    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    products = [p for p in products if p["id"] != product_id]

    return jsonify({"message": "Product deleted"})


if __name__ == "__main__":
    app.run(debug=True)
