from pymongo import MongoClient


def search_mongo(table_name, id_field, id, db_url="localhost", db_port=270127):
    client = MongoClient(db_url, db_port)
    db = client["northwind"]
    table = db[table_name]
    return [doc for doc in table.find({id_field: id})]


def example():
    print(search_mongo("order_details", "order_id", 10248))
    print(search_mongo("products", "product_id", 20))
