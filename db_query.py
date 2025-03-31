from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import Optional



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