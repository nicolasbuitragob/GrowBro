import sqlite3
import os
from datetime import datetime
from typing import Annotated

from sqlmodel import Field, Session, SQLModel, create_engine, select
from dotenv import load_dotenv
load_dotenv()



with sqlite3.connect(os.getenv('DB_FILE')) as connection:

    # Create a cursor object
    cursor = connection.cursor()

    # Write the SQL command to create the Students table
    create_plants_table_query = '''
    CREATE TABLE IF NOT EXISTS plants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    '''

    create_records_table_query = '''
    CREATE TABLE IF NOT EXISTS moisture_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        plant_id INTEGER NOT NULL,
        moisture_level FLOAT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (plant_id) REFERENCES plants(id)
        );
    '''



    # Execute the SQL command
    cursor.execute(create_plants_table_query)
    cursor.execute(create_records_table_query)

    # Commit the changes
    connection.commit()

    # Print a confirmation message
    print("Tables created successfully!")


