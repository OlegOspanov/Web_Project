from database import session, User


class CrudUser():
    def create(self,name):
        user = User(name=name)
        session.add(user)
        session.commit()
        session.close()
        return 'Пользователь успешно добавлен'

    def get_users(self):
        users = session.query(User).all()
        return users

    def get_one(self,name):
        user = session.query(User).filter_by(name=name).first()
        if user:
            return user
        else:
            return False


    def update(self,n,name):
        user = session.query(User).filter_by(id=n).first()
        user.name = name
        session.commit()
        session.close()

    def delete(self,name):
        user = session.query(User).filter_by(name=name).first()
        session.delete(user)
        session.commit()
        session.close()
        return {'succses':True,'message':f"Имя {user.name} успешно удалено"}