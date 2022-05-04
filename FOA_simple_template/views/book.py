from regex import B
from models.book import Book
from schemas.book import BookBody, BookBodyDeserializer

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
    return {"code": 0, "message": "ok", "datas": [{**d}]}
