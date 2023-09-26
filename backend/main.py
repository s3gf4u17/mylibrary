from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import create_engine,Column,String,or_
from pydantic import BaseModel
from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:nokiarecruitment@192.46.233.90:5432/nokia"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

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

def get_books(db:Session,skip:int=0,limit:int=10,query:str=""):
    return db.query(BookModel).filter(or_(BookModel.title.icontains(query),BookModel.author.icontains(query))).offset(skip).limit(limit).all()

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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