from fastapi import FastAPI, HTTPException
from BookService import BookService
from pydantic import BaseModel

app = FastAPI(title="Books API")
book_repository = BookService()


class BookSaveRequest(BaseModel):
    client_id: int
    isbn: int


def save(client_id,book):
    pass


@app.get("/isbn/{isbn}")
async def get_book_by_isbn(isbn: int):
    try:
        return book_repository.book_by_isbn(isbn)
    except:
        raise HTTPException(status_code=404, detail="Book not found")


@app.get("/works/{work_id}")
async def get_work_by_id(work_id: str):
    try:
        return book_repository.work_by_id(work_id)
    except:
        raise HTTPException(status_code=404, detail="Work not found")


@app.post("/save")
async def save_isbn(request: BookSaveRequest):
    book = {}
    try:
        book = book_repository.book_by_isbn(request.isbn)
    except:
        raise HTTPException(status_code=400, detail="Invalid ISBN")
    save(request.client_id,book)

    return request
