from flask import Flask
import json
from about import me
from data import mock_data
from collections import Counter

app = Flask("__server__") #create instance of flask class

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
    return json.dumps(mock_data)

@app.get("/api/products/count")
def total_products():
    return json.dumps(f'{len(mock_data)}')

@app.get("/api/developer/name")
def developer_name():
    return json.dumps(f'{me["name"]} {me["last_name"]} -- {me["email"]}')

@app.get("/api/categories")
def categories():
    cat=[];
    for item in mock_data:
        if not(cat.count(item['category'])):
            cat.append(item['category'])
    # counts = Counter(cat)
    # cat=list(counts.keys())

    return json.dumps(f'{cat}')

@app.get("/api/products/total")
def total_amount():
    total=0
    for item in mock_data:
        total+=item['price']
    return json.dumps(f'The total price is: {total}')

@app.get("/api/catalog/<category>")
def products_by_category(category):
    data=[]
    for item in mock_data:
        if(item["category"]==category):
            data.append(item)
    return json.dumps(f'{data}')


app.run(debug=True)