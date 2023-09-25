import csv

with open('query.sql','w+') as queryfile:
    queryfile.write("""CREATE TABLE books (
        id PRIMARY_KEY NOT NULL TEXT,
        title TEXT,
        author TEXT,
        rating TEXT,
        isbn TEXT,
        isbn13 TEXT,
        lang TEXT,
        pages TEXT,
        publication_date TEXT,
        publisher TEXT
    );\n""")

    with open('books.csv','r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        next(reader,None)
        for row in reader:
            elements = [element.replace('\'','') for element in row]
            queryfile.write(f"""INSERT INTO books VALUES(
                '{elements[0]}','{elements[1]}','{elements[2]}','{elements[3]}','{elements[4]}',
                '{elements[5]}','{elements[6]}','{elements[7]}','{elements[10]}','{elements[11]}'
            );\n""")