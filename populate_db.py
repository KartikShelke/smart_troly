from app import db, Product, app

def populate_database():
    with app.app_context():
        # Add sample products
        products = [
            Product(name='Milk', quantity=50, price=50.0, barcode='1234567890123'),
            Product(name='Bread', quantity=30, price=30.0, barcode='9876543210987'),
            Product(name='Eggs', quantity=100, price=5.0, barcode='1122334455667')
        ]

        db.session.bulk_save_objects(products)
        db.session.commit()
        print("Database populated with sample products!")

if __name__ == "__main__":
    populate_database()