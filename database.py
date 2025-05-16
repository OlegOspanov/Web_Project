from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    first_name = Column(String)
    second_name = Column(String)
    email = Column(String)
    password = Column(String)



class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer,primary_key=True)
    title = Column(String)
    author = Column(String)
    available = Column(Boolean)

class Admin(Base):
    __tablename__ = 'Admin'

    id = Column(Integer,primary_key=True)
    login = Column(String)
    password = Column(String)
    email = Column(Integer)

Base.metadata.create_all(engine)





