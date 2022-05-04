from pydantic import BaseModel



class BookBody(BaseModel):
    age: int
    author: str