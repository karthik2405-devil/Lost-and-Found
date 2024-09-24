from fastapi.params import Body
from fastapi import FastAPI,Depends
from pydantic import BaseModel,Field
import time
import psycopg2
from psycopg2.extras import RealDictCursor
from routers import auth,found,lost,match,notification,user_item
from database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session

app=FastAPI()

app.include_router(notification.router)
app.include_router(found.router)
app.include_router(match.router)
app.include_router(auth.router)
app.include_router(user_item.router)
app.include_router(lost.router)


while True:

    try:
        conn=psycopg2.connect(host="localhost",database="customer",user="postgres",password="2405",cursor_factory=RealDictCursor)
    # cursor_factory=RealDictCursor this sends the column as the value where as without it it actually sends without column name, sends just the values
        cursor=conn.cursor()
        print("database connection was successful")
        break
    except Exception as error:
        print("connection to database is failed")
        print("Erro r",error)
        time.sleep(2)
