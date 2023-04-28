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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        book_type = request.form.get('book_type')
        last_chapter = request.form.get('last_chapter')
        total_chapters = request.form.get('total_chapters')
        link = request.form.get('link')
        grade = request.form.get('grade')
        status = request.form.get('status')
        notes = request.form.get('notes')
        priority = request.form.get('priority')
        book_type = BookType.query.filter_by(name=book_type).first()
        status = Status.query.filter_by(name=status).first()
        book = Book(title=title, book_type=book_type, last_chapter=last_chapter,
                   total_chapters=total_chapters, grade=grade, link=link, status=status, notes=notes,
                   priority=priority)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('index'))

    
    book_types = [book_type.name for book_type in BookType.query.all()]
    statuses = [status.name for status in Status.query.all()]
    # return render_template('add.html', )
    books = Book.query.all()

    
    return render_template('Lista.html',
                           books=books,
                           book_types=book_types,
                           statuses=statuses,
                           **indexVariables)
    # return('testing')


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        book_type = request.form.get('book_type')
        last_chapter = request.form.get('last_chapter')
        total_chapters = request.form.get('total_chapters')
        link = request.form.get('link')
        grade = request.form.get('grade')
        status = request.form.get('status')
        notes = request.form.get('notes')
        priority = request.form.get('priority')
        book_type = BookType.query.filter_by(name=book_type).first()
        status = Status.query.filter_by(name=status).first()
        book = Book(title=title, book_type=book_type, last_chapter=last_chapter,
                   total_chapters=total_chapters, grade=grade, link=link, status=status, notes=notes,
                   priority=priority)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('index'))

     
    book_types = [book_type.name for book_type in BookType.query.all()]
    statuses = [status.name for status in Status.query.all()]

    return render_template('add.html', book_types=book_types, statuses=statuses)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

#TODO: Add edit book functionality
#TODO: Add delete book functionality
#TODO: Add search functionality
#TODO: Add sorting functionality
#TODO: Add filtering functionality
#TODO: Import from json