from database import session,Admin

class AdminService:
    def create(self,*args):#
        login,password,email = args
        book = Admin(login=login,password=password,email=email)
        session.add(book)
        session.commit()
        session.close()
        return {'succses': True, 'message': 'Запись добавлена'}

    def read(self):
        admins = session.query(Admin).all()
        try:
            return admins
        except:
            return {'succses': False,'message':f"не удалось получить базу"}
        finally:
            session.close()

    def update(self,id,login,password,email):
        admin = session.query(Admin).filter_by(id=id).first()
        admin.password = password
        admin.login = login
        admin.email = email
        try:
            session.commit()
            return {'succses': True, 'message': f"Запись упешно обновлена"}
        except:
            return {'succses': False,'message':f"Запись не обновлена"}
        finally:
            session.close()

    def delete(self,id):
        admin = session.query(Admin).filter_by(id=id).first()
        try:
            session.delete(admin)
            session.commit()
            return {'succses': True, 'message': f"Запись упешно удалена"}
        except:
            return {'succses': False,'message':f"Запись не удалена"}
        finally:
            session.close()


