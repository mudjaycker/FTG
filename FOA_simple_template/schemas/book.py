from pydantic import BaseModel, StrictStr



class BookBody(BaseModel):
    age: int
    author: StrictStr

class BookBodyDeserializer(BaseModel):
    id_: int
    age: int
    author: StrictStr