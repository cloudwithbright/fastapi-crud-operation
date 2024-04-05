## Import Modules
from src.configs.create_tables import engine, Base
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
def on_startup(app: FastAPI):
    Base.metadata.create_all(bind=engine)
