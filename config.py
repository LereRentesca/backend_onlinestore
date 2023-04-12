import pymongo
import certifi

conn_str = "mongodb+srv://fsdi:admin@cluster0.mowbttg.mongodb.net/?retryWrites=true&w=majority";

client = pymongo.MongoClient(conn_str, tlsCAFile=certifi.where())
db = client.get_database("onlinestore")