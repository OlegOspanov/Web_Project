from database import session, Book

class CrudBook():
    def createbook(self,title,author,available):
        book = Book(title=title,author=author,available=available)
        session.add(book)
        session.commit()
        session.close()
        return{'succses':True,'message':'Книга успешно добавлена'}

    def read_all(self):
        book = session.query(Book).all()
        return book

    def update(self,id,title,author,available):
        book = session.query(Book).filter_by(id=id).first()
        book.title=title
        book.author=author
        book.available=available
        try:
            session.commit()
            return {'sucsses':True,"message":"Запись обновлена"}
        except:
            return {'sucsses':False,"message":"Не удалось обновить запись"}
        finally:
            session.close()

    def delete(self,id):
        book = session.query(Book).filter_by(id=id).first()
        try:
            session.delete(book)
            session.commit()
            return {'sucsses': True, "message": "Запись удалена"}
        except:
            return {'sucsses':False,"message":"Не удалось удалить"}
        finally:
            session.close()
