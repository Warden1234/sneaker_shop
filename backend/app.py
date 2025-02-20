from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity,create_access_token, jwt_required
import secrets
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
 
app = Flask(__name__)
CORS(app)  

# MongoDB connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/shoe_store"  
app.config["JWT_SECRET_KEY"] = secrets.token_hex(32) 

mongo = PyMongo(app)
jwt = JWTManager(app)

mongo.db.users.create_index("username", unique=True)
mongo.db.baskets.create_index("user_id")
mongo.db.products.create_index("category")

@app.route('/updateQuantity', methods=['PATCH'])
@jwt_required()
def update_quantity():
    data = request.get_json()
    user_id = get_jwt_identity()['user_id']  

    item_id = data.get('item_id')
    new_quantity = int(data.get('quantity'))

    if not item_id or new_quantity is None:
        return jsonify({"error": "Missing item_id or quantity"}), 422

    if new_quantity < 1:
        return jsonify({"error": "Quantity must be at least 1"}), 400

    basket = mongo.db.baskets.find_one({"user_id": user_id})

    if not basket:
        return jsonify({"error": "Basket not found"}), 404

    for item in basket['items']:
        if item['item_id'] == item_id:
            item['quantity'] = new_quantity
            break
    else:
        return jsonify({"error": "Item not found in basket"}), 404

    mongo.db.baskets.update_one({"user_id": user_id}, {"$set": {"items": basket['items']}})
    return jsonify({"message": "Quantity updated successfully"}), 200


@app.route('/removeItem', methods=['DELETE'])
@jwt_required()
def remove_item():
    data = request.get_json()
    user_id = get_jwt_identity()['user_id']  

    item_id = data.get('item_id')

    if not item_id:
        return jsonify({"error": "Missing item_id"}), 422

    # Find the user's basket
    basket = mongo.db.baskets.find_one({"user_id": user_id})

    if not basket:
        return jsonify({"error": "Basket not found"}), 404

    # Remove the item
    basket['items'] = [item for item in basket['items'] if item['item_id'] != item_id]
    print(basket['items'])
    mongo.db.baskets.update_one({"user_id": user_id}, {"$set": {"items": basket['items']}})
    return jsonify({"message": "Item removed successfully"}), 200

@app.route('/addToBasket', methods=['POST'])
@jwt_required()
def add_to_basket():
    user_id = get_jwt_identity()['user_id']  # Extract user_id from JWT
    data = request.get_json()
    print(data)

    item_id = data.get('item_id')
    name = data.get('name')
    price = float(data.get('price'))
    quantity = int(data.get('quantity'))
    image_url=data.get('image_url')

    if not (item_id and name and price and quantity):
        return jsonify({"error": "Missing required fields"}), 400

    # Find the user's basket
    basket = mongo.db.baskets.find_one({"user_id": user_id})

    if basket:
        # Check if the item already exists
        for item in basket['items']:
            if item['item_id'] == item_id:
                item['quantity'] += quantity  # Update quantity
                break
        else:
            # Add new item
            basket['items'].append({
                "item_id": item_id,
                "name": name,
                "price": price,
                "image_url": image_url,
                "quantity": quantity
            })
        # Update the basket in the database
        mongo.db.baskets.update_one(
            {"user_id": user_id},
            {"$set": {"items": basket['items']}}
        )
    else:
        # Create a new basket for the user
        mongo.db.baskets.insert_one({
            "user_id": user_id,
            "items": [{
                "item_id": item_id,
                "name": name,
                "price": price,
                "image_url": image_url,
                "quantity": quantity
            }]
        })

    return jsonify({"message": "Item added to basket"}), 200


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = generate_password_hash(data.get('password'))

    if mongo.db.users.find_one({"username": username}):
        return jsonify(message="Username already exists"), 400

    mongo.db.users.insert_one({
        "username": username,
        "password": password,
    })
    return jsonify(message="User registered successfully"), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = mongo.db.users.find_one({"username": data['username']})
    if user and check_password_hash(user['password'], data['password']):
        access_token = create_access_token(identity={"user_id": str(user['_id']), "username": user['username']})
        return jsonify(access_token=access_token)
    return jsonify(message="Invalid credentials"), 401


@app.route("/createOrder", methods=['POST'])
@jwt_required()
def createOrder():
    user_id = get_jwt_identity()['user_id']
    basket = mongo.db.baskets.find_one({"user_id": user_id})
    
    if not basket:
        return jsonify({"error": "Basket not found"}), 404
    
    items=basket['items']
    total_price = sum( float(item['price']) * int(item['quantity']) for item in items)
    orderStatus= "created"
    paymentStatus="Confirmed"
    createdAt= datetime.datetime.now()
    mongo.db.orders.insert_one({
        "user_id": user_id,
        "items": items,
        "total_price": total_price,
        "orderStatus": orderStatus,
        "paymentStatus": paymentStatus,
        "createdAt": createdAt
    })

    mongo.db.baskets.delete_one({"user_id": user_id})
    
    return jsonify({"message": "Order was successfully created!"}), 200



@app.route('/products', methods=['GET'])
def get_products():
    category = request.args.get('category', None)
    if category:
        products = list(mongo.db.products.find({'category': category}))
    else:
        products = list(mongo.db.products.find())

    for product in products:
        product['_id'] = str(product['_id'])

    return jsonify(products)


@app.route('/basket', methods=['GET'])
@jwt_required()
def get_basket():
    user_id = get_jwt_identity()['user_id']  

    basket = mongo.db.baskets.find_one({"user_id": user_id})
    if not basket:
        return jsonify(items=[]), 200 

    basket["_id"] = str(basket["_id"])  
    return jsonify(basket), 200

@app.route('/orders', methods=['GET'])
@jwt_required()
def get_orders():
    user_id = get_jwt_identity()['user_id']  

    orders = mongo.db.orders.find({"user_id": user_id})
    orders=list(orders)
    print(orders)
    if not orders:
        return jsonify(items=[]), 200 

    for order in orders:
        order["_id"] = str(order["_id"]) 

    return jsonify(items=orders), 200


if __name__ == '__main__':
    app.run(debug=True)
