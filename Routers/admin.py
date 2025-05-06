from sys import prefix

from fastapi import APIRouter,Form

from Services.admin import AdminService
from DTO.admin import AdminSchema

admin = AdminService()

router = APIRouter(prefix='/Admin',tags=['Admin'])

@router.post('/admin',summary='Добовление')
def create_admin(data:AdminSchema):
    return admin.create(data.login,data.password,data.email)

@router.post('/submit')
def create_admin(login:str = Form()):
    return admin.create(login = login,password = password,email = email)

@router.get('/admin',summary='Получение базы данных')
def get_admin():
    return admin.read()

@router.put('/admin{id}',summary='Обновление записи админа')
def update_admin(id,login,password,email):
    return admin.update(id,login,password,email)

@router.delete('/admin{id}',summary='Удаление администратора')
def delete_admin(id):
    return admin.delete(id)