from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Supplier(db.Model):
    __tablename__ = 'supplier'
    id = db.Column(db.Integer, primary_key=True)  # otomatis auto-increment
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100))

    products = db.relationship('Product', backref='supplier', lazy=True)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)  # otomatis auto-increment
    name = db.Column(db.String(100), nullable=False)

    products = db.relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)  # otomatis auto-increment
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
