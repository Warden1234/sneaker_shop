# Sneaker Shop


## Overview

Sneaker Shop is a full-stack e-commerce web application designed for sneaker enthusiasts. This platform provides a seamless shopping experience where users can browse an extensive collection of sneakers, add products to their cart, and place orders securely. The system supports user authentication, order history tracking, and a modern, responsive UI built with Vue.js. The application is built using Vue.js for the frontend and Flask for the backend, with MongoDB as the database.
The project is fully open-source and can be customized to fit other responses.

## Features

* **User authentication** (Registration & Login)

* **Product browsing by category**

* **Shopping cart management** (Add, Update, Remove items)

* **Order processing and checkout**

* **Secure JWT-based authentication**

* **Admin functionalities (future scope)**

## Technologies Used

### Frontend

* Vue.js (Composition API)

* Axios for API calls

* Bulma CSS framework

### Backend

* Flask (Python)

* Flask-PyMongo for MongoDB integration

* Flask-JWT-Extended for authentication

* Flask-CORS for cross-origin support

* Werkzeug for password hashing

### Database

* MongoDB for user, product, and order data storage
The structure of mongodb must consist of 4 collections: baskets,orders,products, users.
Structure of each collections:
**Users**
  ```
  username: String,
  password: String
  ```

**baskets**
  ```
  user_id: String,
  items: Array[{
      itemId:String,
      name:String,
      price:Double,
      image_url:String,
      quantity:Integer
}]
  ```

**shoes**
  ```
  name: String,
  brand: String,
  price: Double,
  category: String,
  Description:String
  ```

**orders**
  ```
  user_id: String,
  items: Array[{
      itemId:String,
      name:String,
      price:Double,
      image_url:String,
      quantity:Integer
}]
  totalPrice: Double,
  orderStatus: String,
  paymentStatus: String,
  createdAt: Timestamp
  ```
### ERD Diagram of the DataBase:
![image](https://github.com/user-attachments/assets/6d2e64ea-ebb8-4bbc-b1ca-393340e133ae)


## Installation

### Prerequisites

Ensure you have the following installed:

* **Python (3.7+)**

* **Node.js & npm**

* **MongoDB**

### Backend Setup

1) Clone the repository:
``` bash
git clone https://github.com/yourusername/sneaker-shop.git
cd sneaker-shop/backend
```

Create a virtual environment and activate it:

``` bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Start MongoDB (if not running):

``` bash
mongod --dbpath <your-db-path>
```

Run the Flask server:
``` bash
python app.py
```

### Frontend Setup

Navigate to the frontend directory:

``` bash
cd ../frontend
```

Install dependencies:

``` bash
npm install
```

Run the development server:

``` bash
npm run dev
```

## API Endpoints

Authentication

POST ```/register``` - Register a new user

POST ```/login``` - Authenticate user & return JWT token

Products

GET ```/products``` - Fetch all products (with optional category filter)

Cart

POST ```/addToBasket``` - Add an item to the cart

PATCH ```/updateQuantity``` - Update item quantity in cart

DELETE ```/removeItem``` - Remove an item from cart

GET ```/basket``` - Get current user's cart

Orders

POST ```/createOrder``` - Create an order from the cart

GET ```/orders``` - Fetch all orders of the user

## Usage

* Register or log in to the application.

* Browse sneakers and add items to your cart.

* Manage your cart (update quantities or remove items).

* Checkout to place an order.

* View order history.

## Future Improvements

* Implement an admin panel for product management

* Add payment gateway integration

* Implement order tracking

* Improve UI/UX



## Contact

For any inquiries or contributions, reach out via email at srlk04@mail.ru or open an issue on GitHub.
