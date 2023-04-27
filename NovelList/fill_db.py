import psycopg2
from pathlib import Path
from dotenv import dotenv_values
import json

def ReadFromJson():
    with (open(Path('lista.json'), 'r', encoding='utf-8')) as f:
        cur = conn.cursor()
        for line in json.load(f):
            print(line)
            cur.execute('INSERT INTO "Lista" (nazwa, typ, rozdzialy, rozdzialySPE, ocena, status, notatka, link)'
                        'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                        (line['title'],
                        line['bookType'],
                        489,
                        'A great classic!')
           )

cur.execute('CREATE TABLE "Lista" (id serial PRIMARY KEY,'
                                        'nazwa varchar (250) NOT NULL,'
                                        'typ varchar (50) NOT NULL,'
                                        'rozdzialy integer NOT NULL,'
                                        'rozdzialySPE varchar (100),'
                                        'ocena integer,'
                                        'status varchar (100),'
                                        'notatka text,'
                                        'link varchar (250));')
config = dotenv_values(".env")

conn = psycopg2.connect(
        host="localhost",
        database="novelkiFlask",
        user=config['USER'],
        password=config['PASSWORD'])

# # Open a cursor to perform database operations
cur = conn.cursor()
ReadFromJson()
# # cur.execute('INSERT INTO books (title, author, pages_num, review)'
# #             'VALUES (%s, %s, %s, %s)',
# #             ('A Tale of Two Cities',
# #              'Charles Dickens',
# #              489,
# #              'A great classic!')
# #             )

# conn.commit()

cur.close()
conn.close()