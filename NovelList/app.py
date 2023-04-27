from flask import Flask, render_template, request, redirect, url_for, session, flash, current_app, g
from dotenv import dotenv_values
from models import Book, BookType, Status
from database import db

config = dotenv_values(".env")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASE_URL']
db.init_app(app)
with app.app_context():
    db.create_all()

indexVariables = {
    'title': 'Baza danych Novelek',
    'heading': 'Novelki'
}

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('Lista.html', books=books, **indexVariables)
    # return('testing')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        book_type = request.form.get('book_type')
        last_chapter = request.form.get('last_chapter')
        total_chapters = request.form.get('total_chapters')
        frequency = request.form.get('frequency')
        status = request.form.get('status')
        notes = request.form.get('notes')
        priority = request.form.get('priority')
        book_type = BookType.query.filter_by(name=book_type).first()
        status = Status.query.filter_by(name=status).first()

        book = Book(title=title, book_type=book_type, position=position, last_chapter=last_chapter,
                   total_chapters=total_chapters, frequency=frequency, status=status, notes=notes,
                   priority=priority)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('book_list'))

    print(BookType.query.all())
    app.logger.info(BookType.query.all())
    book_types = [book_type.name for book_type in BookType.query.all()]
    statuses = [status.name for status in Status.query.all()]

    return render_template('add_book.html', book_types=book_types, statuses=statuses)


@app.route('/book_list')
def book_list():
    books = Book.query.all()
    return render_template('book_list.html', books=books)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')