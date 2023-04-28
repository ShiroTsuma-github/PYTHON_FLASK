from pathlib import Path
from dotenv import dotenv_values
import json
from models import Book, BookType, Status
from database import db
from flask import Flask

config = dotenv_values(".env")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASE_URL']
db.init_app(app)
with app.app_context():
    db.create_all()

def ReadFromJson():
    with (open(Path('lista.json'), 'r', encoding='utf-8')) as f:
        with app.app_context():
            for line in json.load(f):
                print(line)
                book_type = BookType.query.filter_by(name=line['bookType']).first()
                status = Status.query.filter_by(name=line['status'] if line['status'] != '' else 'Reading').first()
                book = Book(title=line['title'],
                            book_type = book_type,
                            last_chapter=line['lastChapter'],
                            total_chapters=line['totalChapters'],
                            status=status,
                            notes=line['notes'],
                            priority=line['priority'],
                            link=''
                            )
                db.session.add(book)
            db.session.commit()





# book = Book(title=title, book_type=book_type, last_chapter=last_chapter,
#             total_chapters=total_chapters, frequency=frequency, status=status, notes=notes,
#             priority=priority)
ReadFromJson()

