from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from os import getenv
from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    sql_path = "db.sql"

    try:
        with open(sql_path, 'r') as f:
            sql_script = f.read()
        
        with engine.connect() as connection:
            with connection.begin():
                connection.execute(text(sql_script))

        print("Database initialization complete")
    except Exception as e:
        print(f"Error initializing database: {str(e)}")



if __name__ == "__main__":
    init_db()