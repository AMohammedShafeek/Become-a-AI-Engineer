from fastapi import FastAPI
from sqlalchemy import text
from app.db.database import engine

app = FastAPI()


@app.get("/")
def root():
    return {"message": "01-password-hashing"}

@app.get("/health")
def health():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database();")
        )

        db_name = result.scalar()
    return {
        "database": db_name,
        "status": "true",
        "mesage": "DB Connected"
    }
    