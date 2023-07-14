import pandas as pd 
from insertIntoMongo import df_mongo
from saveLocal import write_json

def import_csv(csv_path):
    df = pd.read_csv(csv_path, header=0)
    table_name = 'order_details'
    write_json(df, 'csv', table_name)
    df_mongo(df, table_name)

def call_import(): import_csv('data/order_details.csv')
