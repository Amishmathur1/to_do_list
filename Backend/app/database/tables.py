import os
import psycopg
from dotenv import load_dotenv

load_dotenv() #Always load the .env file before using its features

db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

conn = psycopg.connect(**db_config)

def user_detail_store(email, password):
    sql = '''
        INSERT INTO users (email, password, created_at)
        VALUES (%s, %s, NOW());
        '''
    try:
        with conn.cursor() as curr:
            curr.execute(sql, (email, password))
            conn.commit()

    except (Exception, psycopg.DatabaseError) as error:
        conn.rollback()
        return error
