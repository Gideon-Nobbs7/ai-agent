from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic import BaseModel
from sqlalchemy.orm import Session
from dataclasses import dataclass
from typing import List, Union
from db_query import AgentDbConn
from database import get_db
from utils import extract_details
from os import getenv
from dotenv import load_dotenv
import asyncio



load_dotenv()


provider = OpenAIProvider(
        base_url=getenv("OPENROUTER_BASE_URL"),
        api_key=getenv("OPENROUTER_API_KEY")
)

model = OpenAIModel(
    "openai/gpt-3.5-turbo",
    provider=provider
)


system_prompt = """
                You are an assistant in our shop. Answer our customers with the answers you have.
                If you do not have an answer to a question, tell them to call us.
                Lastly, greet everyone with polite words.
                """

@dataclass
class SupportDependencies:
    db: Session = next(get_db())


class ConversationMessage(BaseModel):
    role: str
    content: str

    
class ResponseModel(BaseModel):
    name: str
    category: str
    price: float
    
    class Config:
        arbitrary_types_allowed = True


class ProductSearchResponse(BaseModel):
    products: List[ResponseModel]


class ProductSearchError(BaseModel):
    error_message: str


SearchResponse = Union[ProductSearchResponse, ProductSearchError]


agent= Agent(
    model=model,
    deps_type=SupportDependencies,
    system_prompt=system_prompt
)


@agent.tool
async def get_product_by_name(ctx:RunContext[SupportDependencies]):
    """
    Search the database for the details of a product.

    Args:
        ctx: The context containing the products
    """
    
    prompt = ctx.prompt.lower()
    product_name, _ = extract_details(prompt)

    product = AgentDbConn.get_product_by_name(db=ctx.deps.db, name=product_name)
    return product
    # return ProductSearchResponse(
    #     products=[
    #         ResponseModel(
    #             name=product['name'],
    #             price=product['price'],
    #             category=product['category']
    #         )
    #     ]
    # )


@agent.tool
async def get_product_by_category(ctx:RunContext[SupportDependencies]):
    """
    Search the database for the details of a product.

    Args:
        ctx: The context containing the products
    """
    prompt = ctx.prompt.lower()
    product_name, _ = extract_details(prompt)
    product = AgentDbConn.get_product_by_category(db=ctx.deps.db, category=product_name)
    return product
    # return ProductSearchResponse(
    #     products=[
    #         ResponseModel(
    #             name=product['name'],
    #             price=product['price'],
    #             category=product['category']
    #         )
    #     ]
    # )


@agent.tool
async def get_product_by_budget(ctx:RunContext[SupportDependencies]):
    """
    Search the database for the details of a product based on a budget.

    Args:
        ctx: The context containing the products
    """
    prompt = ctx.prompt.lower()
    _, budget = extract_details(prompt)

    product = AgentDbConn.get_product_by_budget(db=ctx.deps.db, budget=budget)
    return product


class AIAssistant:
    def __init__(self):
        self.deps = SupportDependencies()
        self.conversation_history: List[ConversationMessage] = []

    async def process_meessage(self, user_input: str):
        self.conversation_history.append(
            ConversationMessage(role="assistant", content=user_input)
        )

        result = await agent.run(user_prompt=user_input, deps=self.deps)

        if isinstance(result.data, ProductSearchError):
            response = result.data.error_message
        else:
            response = result.data
        return response
    

async def main():
    assistant = AIAssistant()
    
    while True:
        user_input = await asyncio.to_thread(input, "Enter a prompt to interact with your data: ")

        if user_input.lower() in {"exit", "quit"}:
            break 

        response = await assistant.process_meessage(user_input=user_input)
        print(response)


if __name__ == "__main__":
    asyncio.run(main())