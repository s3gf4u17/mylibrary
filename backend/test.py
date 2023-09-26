from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_404():
    response = client.get("/books/")
    assert response.status_code == 404

def test_limit_0():
    response = client.get("/?limit=0")
    assert response.status_code == 200
    assert response.json() == []

def test_query_ruby_cookbook():
    response = client.get("/?query=ruby cookbook")
    assert response.status_code == 200
    assert response.json() == [{"id":"141","title":"Ruby Cookbook","author":"Lucas Carlson/Leonard Richardson","rating":"3.84","isbn":"0596523696","isbn13":"9780596523695","lang":"eng","pages":"873","publication_date":"7/29/2006","publisher":"OReilly Media"}]

def test_query_atlantis_skip_2():
    response = client.get("/?query=atlantis&skip=2")
    assert response.status_code == 200
    assert response.json() == [{"id":"41707","title":"Atlantis Found (Dirk Pitt  #15)","author":"Clive Cussler","rating":"3.99","isbn":"0425204030","isbn13":"9780425204030","lang":"eng","pages":"530","publication_date":"10/26/2004","publisher":"Berkley Trade"}]

def test_AUTHOR_Martin_Kalin():
    response = client.get("/?query=author:martin kalin")
    assert response.status_code == 200
    assert response.json() == [{"id":"1771","title":"Object-Oriented Programming in C++","author":"Richard Johnsonbaugh/Martin Kalin","rating":"4.07","isbn":"0130158852","isbn13":"9780130158857","lang":"eng","pages":"640","publication_date":"8/13/1999","publisher":"Prentice Hall"}]

def test_TITLE_Trust_Fund():
    response = client.get("/?query=title:trust fund")
    assert response.status_code == 200
    assert response.json() == [{"id":"26289","title":"Trust Fund","author":"Stephen W. Frey","rating":"3.72","isbn":"0345428307","isbn13":"9780345428301","lang":"eng","pages":"358","publication_date":"1/2/2002","publisher":"Fawcett Books"}]

def test_multiple():
    response = client.get("/?query=title:rowling&limit=2")
    assert response.status_code == 200
    assert response.json() == [{"id":"1999","title":"J.K.Rowling","author":"Colleen Sexton","rating":"3.84","isbn":"0822533898","isbn13":"9780822533894","lang":"eng","pages":"112","publication_date":"9/1/2005","publisher":"Lerner Publications"},{"id":"2004","title":"J.K. Rowlings Harry Potter Novels: A Readers Guide","author":"Philip Nel","rating":"3.58","isbn":"0826452329","isbn13":"9780826452320","lang":"eng","pages":"96","publication_date":"9/26/2001","publisher":"Bloomsbury Academic"}]