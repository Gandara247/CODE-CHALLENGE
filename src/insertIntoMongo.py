from pymongo import MongoClient, ASCENDING, errors
import json
from constants import table_idx, table_relationsships


def df_mongo(df, table_name, db_url= 'localhost', db_port=270127):
    payload = json.loads(df.to_json(orient='records'))
    clients = MongoClient(db_url, db_port)
    db = clients['northwind']
    table = db[table_name]
    primary_keys = table_idx[table_name]
    foreign_keys = table_relationsships.get(table_name, [])

    indexes = [(col, ASCENDING) for col in primary_keys]
    table.create_index(indexes, unique=True)

    try:
        table.insert_many(payload)
        add_child_tables(table, foreign_keys, table_name)

    except errors.BulkWriteError as err:
        find_duplicate_keys(err)

def add_child_tables(table, foreign_keys, table_name):
    print(table_name)
    pipeline = []
    for child in foreign_keys:
        idx = table_idx[child][0]
        pipeline.append({
            '$lookup': {'from': child, 'localField': idx, 'foreignField': idx, 'as': child}
        })
    cur = table.aggregate(pipeline)
    for doc in cur:
        print(doc)
        table.replace_one({'_id': doc['_id']}, doc)

def find_duplicate_keys(err):
    panic = filter(lambda x: x['code'] != 11000, err.details['writeErrors'])
    if len(panic) > 0:
        raise errors.BulkWriteError(panic)    
