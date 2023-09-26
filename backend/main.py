from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:nokiarecruitment@172.104.227.113:5432/nokia"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

from sqlalchemy import Column,String

class BookModel(Base):
    __tablename__="books"
    id=Column(String,primary_key=True,nullable=False)
    title=Column(String)
    author=Column(String)
    rating=Column(String)
    isbn=Column(String)
    isbn13=Column(String)
    lang=Column(String)
    pages=Column(String)
    publication_date=Column(String)
    publisher=Column(String)

from pydantic import BaseModel

class BookSchema(BaseModel):
    id:str
    title:str
    author:str
    rating:str
    isbn:str
    isbn13:str
    lang:str
    pages:str
    publication_date:str
    publisher:str
    class Config:
        orm_mode = True

from sqlalchemy.orm import Session
from sqlalchemy import or_

def get_books(db:Session,skip:int=0,limit:int=10,query:str=""):
    return db.query(BookModel).filter(or_(BookModel.title.icontains(query),BookModel.author.icontains(query))).offset(skip).limit(limit).all()

Base.metadata.create_all(bind=engine)

from fastapi import Depends,FastAPI
from sqlalchemy.orm import Session

app = FastAPI()

# DEPENDENCY
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/",response_model=list[BookSchema])
def read_books(skip:int=0,limit:int=10,query:str="",Session=Depends(get_db)):
    books = get_books(Session,skip,limit,query)
    return books