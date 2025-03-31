from fastapi import FastAPI, Depends
from pydantic import BaseModel
import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from typing import Optional
from db_query import ProductRepository
from database import init_db, get_db


app = FastAPI()



class ProductModel(BaseModel):
    name: str
    price: float
    category: str


@app.on_event("startup")
async def startup_event():
    init_db()


@app.post("/products/create")
async def create_product(
    product: ProductModel,
    db: Session = Depends(get_db)
):
    repo = ProductRepository(db)
    return repo.create_product(**product.model_dump())


@app.get("/products/list")
async def list_products(
    category: Optional[str] = None,
    price: Optional[float] = None,
    db: Session = Depends(get_db)
):
    repo = ProductRepository(db)
    return repo.list_products(category, price)


@app.get("/products/{id}")
async def get_product_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    repo = ProductRepository(db)
    return repo.get_product_by_id(id)
