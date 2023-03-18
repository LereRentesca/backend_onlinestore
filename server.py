from flask import Flask
import json
from about import me

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

app.run(debug=True)