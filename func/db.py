from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
import pandas as pd
import os

load_dotenv()
DATABASE = os.getenv('DATABASE_URL')


def obtain_data_by_casino(casino):
    query = f"""
    SELECT * FROM "ZIP_CODE_PLAYER_LEVEL" WHERE "Casino" = '{casino}'
"""

    engine = create_engine(DATABASE)
    df = pd.read_sql_query(query, engine)
    engine.dispose()


    return df