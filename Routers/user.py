from sys import prefix
from typing import Annotated

from fastapi import APIRouter,HTTPException,Path,Form

from DTO.user import UserSchema
from Services.user import CrudUser
router = APIRouter()
crud = CrudUser()

@router.post('/users',summary='Добавление пользователей',tags=['Пользователи'])
def create_users(user:UserSchema):
    return crud.create(user.name)


@router.get('/users',summary='Получение списка пользователей',tags=['Пользователи'])
def read_users():
    return crud.get_users()

@router.get('/users/one',summary='Получение списка пользователей',tags=['Пользователи'])
def get_user_one(name):
    return crud.get_one(name)

@router.put('/users/{id}',summary='Изменение имени пользователя',tags=['Пользователи'])
def update_user(id:Annotated[int,Path(ge=1,lt=1_000_000)],name:str):
    return crud.update(id,name)

@router.delete('/users/delete',summary='Удаление пользователя',tags=['Пользователи'])
def delete_user(name):
    return crud.delete(name)

@router.post('/abracadabra',tags=['Пользователи'])
def create_users(data: Annotated[UserSchema,Form()]):
    user = crud.get_one(data.name)
    if user == False:
        return crud.create(data.name)
    else:
        return "Пользователь уже есть в база!"
