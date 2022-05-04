from typing import Optional
from pydantic import BaseModel



class BookBody(BaseModel):
    age: int
    author: str

class BookBodyDeserializer(BaseModel):
    id_: int
    age: int
    author: str