from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 1500},
    {"id": 2, "name": "Phone", "price": 700}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_id = max(p['id'] for p in products) + 1 if products else 1
    product = {"id": new_id, "name": data['name'], "price": data['price']}
    products.append(product)
    return jsonify(product), 201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    for product in products:
        if product['id'] == id:
            product['name'] = data.get('name', product['name'])
            product['price'] = data.get('price', product['price'])
            return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    global products
    products = [p for p in products if p['id'] != id]
    return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
