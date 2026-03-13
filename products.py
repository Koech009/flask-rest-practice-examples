from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Laptop', 'price': 999.99},
    {'id': 2, 'name': 'Smartphone', 'price': 499.99},
    {'id': 3, 'name': 'Headphones', 'price': 199.99}
]

# get all products


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)
# get a single product by id


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
