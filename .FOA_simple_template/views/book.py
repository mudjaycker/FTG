from models.book import Book
from schemas.book import BookBody, BookBodyDeserializer, BookQuery

from flask_openapi3 import APIBlueprint
from flask_openapi3 import Tag

tag = Tag(name="book", description="Some Book")

api = APIBlueprint(
    "/book",
    __name__,
    url_prefix="/api",
    abp_tags=[tag],
    # disable openapi UI
    doc_ui=True,
)

@api.get("/book/<int:id_>")
def get_one(path:BookQuery):
    "get one book"
    b = Book.get_by(path.id_)
    return dict(BookBodyDeserializer(**b.to_json()))

@api.get("/book")
def get_book():
    """Get all Book
    """
    return {
        "books": [dict(BookBodyDeserializer(**b.to_json())) for b in Book.get_all()]
    }


@api.post("/book")
def create_book(body: BookBody):
    "Post a book"
    d = body.dict()
    book = Book(**d)
    book.save_to_db()
    return {"code": 0, "message": "ok", "datas": [d]}


@api.put("/book/<int:id_>")
def update_book(body: BookBody,path:BookQuery):
    "Put a book"

    b = Book.get_by(path.id_)
    b.age = body.age
    b.author = body.author
    b.save_to_db()

    return {"code": 0, "message": "ok", "datas": [dict(body)]}


@api.delete("/book/<int:id_>")
def delete_book(path:BookQuery):
    "delete in book"
    b= Book.get_by(path.id_)
    b.delete_from_db()
    return {"response": "deleted"}
