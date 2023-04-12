from flask import Flask, request
import json
from about import me
from config import db
from collections import Counter
from flask_cors import CORS

app = Flask("__server__") #create instance of flask class
CORS(app) #WARNING: disable CORS check

###METHODS###
def fix_id(record):
    record["_id"]=str(record["_id"])
    return record;

###GET###

@app.get("/")
def home():
    return "Hello World form a flask server"

@app.get("/test")
def test():
    return "This is a test page"


@app.get("/api/version")
def version():
    return json.dumps("1.0")

@app.get("/api/about")
def about():
    return json.dumps(me)

@app.get("/api/catalog")
def catalog():
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        results.append(fix_id(prod))
    return json.dumps(results)

@app.get("/api/coupons")
def coupons():
    coupons = db.coupons.find({})
    results = []
    for prod in coupons:
        results.append(fix_id(prod))
    return json.dumps(results)

@app.get("/api/products/count")
def total_products():
    count = db.products.count_documents({})
    return json.dumps(count)

@app.get("/api/developer/name")
def developer_name():
    return json.dumps(f'{me["name"]} {me["last_name"]} -- {me["email"]}')

@app.get("/api/categories")
def categories():
    cursor = db.products.find({})
    cats = []
    for prod in cursor:
        category = prod["category"]
        if category not in cats:
            cats.append(category)
    return json.dumps(cats)

@app.get("/api/products/total")
def total_amount():
    cursor = db.products.find({})
    total=0
    for prod in cursor:
        total+=prod['price']
    return json.dumps(f'The total price is: {total}')

@app.get("/api/products/lower/<price>")
def products_lower(price):
    fixed_price = float(price)
    cursor = db.products.find({})
    results=[]
    for prod in cursor:
        if prod["price"]<fixed_price:
            results.append(fix_id(prod))
    return json.dumps(results)

@app.get("/api/products/greater/<price>")
def products_greater(price):
    fixed_price = float(price)
    cursor = db.products.find({})
    results=[]
    for prod in cursor:
        if prod["price"] >= fixed_price:
            results.append(fix_id(prod))
    return json.dumps(results)

@app.get("/api/products/search/<term>")
def search(term):
    cursor = db.products.find({"title":{'$regex':term,"$options":"i"}})
    data=[]
    for item in cursor:
        data.append(fix_id(item))
    return json.dumps(data)

@app.get("/api/catalog/<category>")
def products_by_category(category):
    cursor = db.products.find({"category":category})
    results = []
    for prod in cursor:
        results.append(fix_id(prod))
    return json.dumps(results)

@app.get("/api/coupons/<code>")
def coupons_by_code(code):
    cursor = db.coupons.find({"code":code})
    results = []
    for coupon in cursor:
        results.append(fix_id(coupon))
    return json.dumps(results)

###POST#####

@app.post('/api/catalog')
def save_product():
    product = request.get_json()
    db.products.insert_one(product)
    print("-------------------------")
    print(product)

    return json.dumps(fix_id(product))

@app.post('/api/coupons')
def save_coupon():
    coupon = request.get_json()
    db.coupons.insert_one(coupon)
    return json.dumps(fix_id(coupon))

app.run(debug=True)