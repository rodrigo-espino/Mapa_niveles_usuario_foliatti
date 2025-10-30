from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
import pandas as pd
import os

load_dotenv()
DATABASE = os.getenv('DATABASE_URL')


def obtain_data_by_casino(casino, date='2025-01-01'):
    query = f"""
    SELECT * FROM "ZIP_CODE_PLAYER_LEVEL" 
    WHERE "Casino" = '{casino}' AND "LAST_VISIT" >= '{date}'
    """

    engine = create_engine(DATABASE)
    df = pd.read_sql_query(query, engine)
    engine.dispose()


    return df

def obtain_zip_code_players_shared(state):
    query = f"""
    SELECT * FROM "JUGADORES_COMPARTIDOS" WHERE "Estado" = '{state}'
    """
    engine = create_engine(DATABASE)
    df = pd.read_sql_query(query, engine)
    engine.dispose()

    return df