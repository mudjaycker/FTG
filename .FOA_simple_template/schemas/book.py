from pydantic import BaseModel, StrictStr


class BookQuery(BaseModel):
    id_: int


class BookBody(BaseModel):
    age: int
    author: StrictStr

class BookBodyDeserializer(BaseModel):
    id_: int
    age: int
    author: StrictStr