## Import Libries
from fastapi import FastAPI
from src.controller import controller
from src.configs.create_tables import Base, engine
from fastapi.middleware.cors import CORSMiddleware

## Initialize FastAPI
app = FastAPI()

## Create Table (Make sure database exists)
Base.metadata.create_all(bind=engine)

## Add Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## Initialize FastAPI
app.include_router(router=controller.router)
