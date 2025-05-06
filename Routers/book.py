from sys import prefix

from fastapi import APIRouter

from Services.book import CrudBook
from DTO.book import BookSchema
from Services.book import CrudBook


crud = CrudBook()
router = APIRouter(prefix='/books',tags=['Книги'])

@router.post('',summary='Добовление книг')
def create_book(data:BookSchema):
    return crud.createbook(data.title,data.author,data.available)

@router.get('',summary = "get books")
def get_books():
    return crud.read_all()

@router.put('',summary="update book")
def update_book(id,title,author,available):
    return crud.update(id,title,author,available)

@router.delete('',summary="delete book")
def delete_dook(id):
    return crud.delete(id)
