from flask import Flask
from dotenv import dotenv_values
from models import BookType, Status, db
config = dotenv_values(".env")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASE_URL']
db.init_app(app)


# create some initial book types
book_types = ['Novel', 'Manga', 'H-manhwa']
statuses = ['Completed', 'Unknown', 'On hold', 'Abandoned', 'Unsure if discontinued', 'Avoid', 'Reading', 'Plan to read']



with app.app_context():
    for name in book_types:
        book_type = BookType(name=name)
        db.session.add(book_type)
    for name in statuses:
        status = Status(name=name)
        db.session.add(status)
    db.session.commit()
    book_types = BookType.query.all()
    print(book_types)