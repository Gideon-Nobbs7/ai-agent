from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import Optional


# class ProductRepository:
#     def __init__(self, db: Session):
#         self.db = db

    
#     def create_product(self, name: str, price: float, category: str):
#         query = text("""
#                 INSERT INTO products (name, price, category)
#                 VALUES (:name, :price, :category)
#                 RETURNING id, name, price, category, created_at             
#         """)

#         try:
#             result = self.db.execute(query, {
#                 'name': name,
#                 'price': price,
#                 'category': category
#             })
#             self.db.commit()
#             product = result.fetchone()
#             return product._asdict()
#         except Exception as e:
#             self.db.rollback()
#             raise HTTPException(status_code=400, detail=str(e))
    

#     def get_product_by_id(self, product_id: int):
#         query = text("""
#                 SELECT id, name, price, category
#                 FROM products
#                 WHERE id = :product_id
#          """)
        
#         result = self.db.execute(query, {
#             'product_id': product_id
#         })
#         product = result.fetchone()
#         return product._asdict() if product else None


#     def list_products(
#         self, 
#         category: Optional[str] = None,
#         min_price: Optional[float] = None
#     ):
#         query = "SELECT id, name, category, price, created_at FROM products WHERE 1=1"
#         params = {}

#         if category:
#             query += " AND category = :category"
#             params['category'] = category
        
#         if min_price is not None:
#             query += " AND price >= :min_price"
#             params['min_price'] = min_price
        
#         sql_query = text(query)
#         result = self.db.execute(sql_query, params)

#         products = result.fetchall()
#         return [product._asdict() for product in products]



class AgentDbConn:
    
    @staticmethod
    def get_product_by_name(db: Session, name: Optional[str] = None):
        base_query = """
                    SELECT name, category, price 
                    FROM products
                    WHERE name ILIKE :name 
                    """
        query = text(base_query)
        result = db.execute(query, {
            "name": f"%{name}%"
        })
        product = result.fetchone()
        return product._asdict()
    

    @staticmethod
    def get_product_by_category(db: Session, category: str):
        base_query = """
                    SELECT name, category, price 
                    FROM products
                    WHERE category = :category 
                    """
        query = text(base_query)
        result = db.execute(query, {
            "category": category
        })
        product = result.fetchone()
        return product._asdict()
    

    @staticmethod
    def get_product_by_budget(db:Session, budget: int):
        base_query = """
                    SELECT name, category, price 
                    FROM products
                    WHERE price <= :budget 
                    """
        query = text(base_query)
        result = db.execute(query, {
            "budget": budget
        })
        products = result.fetchall()
        return [product._asdict() for product in products]