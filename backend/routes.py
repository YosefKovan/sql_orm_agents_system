from fastapi import Depends, HTTPException
from sqlmodel import Session
from backend.models.login import Login
from fastapi import FastAPI
from project.db.init_db import get_session
from backend.handlers.user_login import handle_login



app = FastAPI()


@app.post("/login")
def login_func(login : Login, session : Session = Depends(get_session)):
     return handle_login(session, login.name, login.password)










