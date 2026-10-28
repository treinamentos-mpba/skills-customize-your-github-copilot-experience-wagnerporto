from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str
    author: str
    year: int


books = [
    {"id": 1, "title": "The Hobbit", "author": "J. R. R. Tolkien", "year": 1937},
    {"id": 2, "title": "Frankenstein", "author": "Mary Shelley", "year": 1818},
]
next_book_id = 3


# TODO: Implement GET /books to return the full collection.

# TODO: Implement POST /books to validate and add a book.

# TODO: Implement GET /books/{book_id} and return 404 when it is missing.

# TODO: Implement PUT /books/{book_id} and DELETE /books/{book_id}.