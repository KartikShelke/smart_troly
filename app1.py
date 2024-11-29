from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    barcode = db.Column(db.String(100), unique=True, nullable=False)

# Initialize Database
def init_db():
    with app.app_context():
        db.create_all()

# Default Route
@app.route('/')
def index():
    return "Welcome to the Smart Cart API! Use the /get-product endpoint to fetch product details."

# API to get product details by barcode
@app.route('/get-product', methods=['POST'])
def get_product():
    data = request.json
    barcode = data.get('barcode')
    product = Product.query.filter_by(barcode=barcode).first()
    if product:
        return jsonify({
            'name': product.name,
            'quantity': product.quantity,
            'price': product.price
        }), 200
    return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    init_db()  # Initialize the database before running the app
    app.run(debug=True)