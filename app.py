from flask import Flask, request, render_template, redirect, url_for
from models import db, Product, Category, Supplier

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    products = Product.query.all()
    categories = Category.query.all()
    suppliers = Supplier.query.all()
    return render_template('index.html',
    products=products,
    categories=categories,
    suppliers=suppliers,
    )
    
@app.route('/products')
def product_list():
    products = Product.query.all()
    return render_template('products.html', products=products)


@app.route('/add_product', methods=['POST'])
def add_product():
    new_product = Product(
        name=request.form['name'],
        price=float(request.form['price']),
        stock=int(request.form['stock']),
        category_id=int(request.form['category_id']),
        supplier_id=int(request.form['supplier_id'])
    )
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_category', methods=['POST'])
def add_category():
    name = request.form['name']
    new_category = Category(name=name)
    db.session.add(new_category)
    db.session.commit()
    return redirect('/')

@app.route('/add_supplier', methods=['POST'])
def add_supplier():
    new_supplier = Supplier(
        name=request.form['name'],
        contact=request.form['contact']
    )
    db.session.add(new_supplier)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
