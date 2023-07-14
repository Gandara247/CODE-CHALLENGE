from sqlalchemy import create_engine
import pandas as pd
from insertIntoMongo import df_mongo
from saveLocal import write_json
from constants import table_idx


def import_postgres():
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/northwind")
    for table_name in table_idx.keys():
        if table_name != "order_details":
            df = pd.read_sql_query(f'select * from "{table_name}"', con=engine)
            if not df.empty:
                write_json(df, 'postgres', table_name)
                df_mongo(df, table_name)
