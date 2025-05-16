from sys import prefix
from typing import Annotated

from fastapi import APIRouter,HTTPException,Path,Form

from DTO.user import UserSchema
from Services.user import CrudUser
router = APIRouter()
crud = CrudUser()

@router.post('/users',summary='Добавление пользователей',tags=['Пользователи'])
def create_users(user:UserSchema):
    return True


@router.get('/users',summary='Получение списка пользователей',tags=['Пользователи'])
def read_users():
    return crud.get_users()

@router.get('/users/one',summary='Получение списка пользователей',tags=['Пользователи'])
def get_user_one(first_name):
    return crud.get_one(first_name)

@router.put('/users/{id}',summary='Изменение имени пользователя',tags=['Пользователи'])
def update_user(id:Annotated[int,Path(ge=1,lt=1_000_000)],first_name:str):
    return crud.update(id,first_name)

@router.delete('/users/delete',summary='Удаление пользователя',tags=['Пользователи'])
def delete_user(first_name):
    return crud.delete(first_name)

@router.post('/abracadabra',tags=['Пользователи'])
def create_users(data: Annotated[UserSchema,Form()]):
    user = crud.get_one(data.first_name)
    if user == False:
        return crud.create(data.first_name,data.second_name,data.email,data.password)
    else:
        return "Пользователь уже есть в база!"
