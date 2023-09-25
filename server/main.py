from fastapi import FastAPI
import csv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data_dict = []
with open("../database/books.csv","r") as database:
    reader = csv.reader(database,delimiter=',')
    next(reader,None)
    for row in reader:
        data_dict.append({
            "id":row[0],
            "title":row[1],
            "author":row[2],
            "rating":row[3],
            "isbn":row[4],
            "isbn13":row[5],
            "language":row[6],
            "pages":row[7],
            "publication_date":row[10],
            "publisher":row[11]
        })

@app.get("/")
def read_root(query:str="",limit:int=10):
    response=[]
    query = query.lower()
    for book in data_dict:
        if query in book["title"].lower() or query in book["author"].lower(): response.append(book)
        if len(response)>=limit: break
    return response