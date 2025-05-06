from typing import Annotated

from fastapi import FastAPI,HTTPException,Path
from pydantic import BaseModel
import uvicorn

from Routers.book import router as book_router
from Routers.admin import router as admin_router
from Routers.user import router as user_router

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import templates

app = FastAPI()
app.include_router(book_router)
app.include_router(admin_router)
app.include_router(user_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='templates')


@app.get("/",summary='Главный метод',tags=['Основновные методы'])
def get_page_index(request: Request):
    return templates.TemplateResponse(name='index.html', context={'request': request})

@app.get("/about",summary='Главный метод',tags=['Основновные методы'])
def get_page_about(request: Request):
    return templates.TemplateResponse(name='about.html', context={'request': request})

if __name__ == '__main__':
    uvicorn.run('main:app')