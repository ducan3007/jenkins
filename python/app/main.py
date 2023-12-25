from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from .config import pool
from fastapi.encoders import jsonable_encoder
from fastapi.logger import logger
import logging
import os

logger = logging.getLogger("uvicorn")

app = FastAPI()

SessionLocal = sessionmaker(bind=pool.engine, autocommit=False, autoflush=False)


@app.get("/")
async def read_root():
    hostname = os.uname()[1]
    return {"Hello": "World", "hostname": hostname}

@app.get("/user")
async def read_user():
    db = SessionLocal()
    logger.info("Fetching users....")
    result = db.execute(text("select * from USER")).fetchall()
    response = []
    for row in result:
        response.append({
            "id": row[0],
            "name": row[1],
            "email": row[2]
        })
    return jsonable_encoder(response)
   


