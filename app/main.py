from fastapi import FastAPI
from .database import init_db
from .routes import setup_routes


app = FastAPI()
db = init_db()
setup_routes(app, db)
