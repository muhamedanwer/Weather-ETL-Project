# load.py
import sqlite3
import pandas as pd
from sqlalchemy import create_engine
import config

def load_to_sqlite(df):
    """
    Load transformed weather data into SQLite database
    """
    # Create SQLite engine
    engine = create_engine(f'sqlite:///{config.DATABASE_PATH}')
    
    # Write to database, append if table exists
    df.to_sql(
        name='weather_data', 
        con=engine, 
        if_exists='append',  # append to existing data
        index=False
    )
    
    print(f"Loaded {len(df)} records to the database.")
    
    return True

def get_connection():
    """
    Get a connection to the SQLite database for queries
    """
    return sqlite3.connect(config.DATABASE_PATH)