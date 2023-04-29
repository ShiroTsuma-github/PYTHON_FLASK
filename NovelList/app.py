from flask import Flask, render_template, request, redirect, url_for, session, flash, current_app, g
from dotenv import dotenv_values
from models import Book, BookType, Status
from database import db
from flask import jsonify

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
        pass
    book_types = [book_type.name for book_type in BookType.query.all()]
    statuses = [status.name for status in Status.query.all()]
    books = Book.query.all()
    return render_template('Lista.html',
                           books=books,
                           book_types=book_types,
                           statuses=statuses,
                           **indexVariables)


@app.route('/add', methods=['POST'])
def add_book():
    if request.method == 'POST':
        if request.form.get('delete') == 'delete':

            book_id = int(request.form.get('bookid'))
            delete_book(book_id)
        elif request.form.get('actionused') == 'edit':
            edit_book(request.form)
        else:
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

    return redirect(url_for('index'))

@app.route('/get_book_details')
def get_book_details():
    book_id = request.args.get('id')
    book = Book.query.get(book_id)
    booktype = BookType.query.get(book.book_type_id)
    status = Status.query.get(book.status_id)
    book_details = {
        'id': book.id,
        'title': book.title,
        'book_type': booktype.name,
        'last_chapter': book.last_chapter,
        'total_chapters': book.total_chapters,
        'link': book.link,
        'grade': book.grade,
        'status': status.name,
        'notes': book.notes,
        'priority': book.priority
        # add more properties here as needed
    }
    return jsonify(book_details)


def delete_book(book_id):
    book = Book.query.filter_by(id=book_id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))

def edit_book(form):
    book_id = int(form['bookid'])
    title = form['title']
    book_type = form['book_type']
    status = form['status']
    total_chapters = int(form['total_chapters'])
    last_chapter = form['last_chapter']
    grade = 0 if form['grade'] == '' else int(form['grade'])
    priority = int(form['priority'])
    link = form['link']
    notes = form['notes']

    
    # Call the update_book function with the form data and book_id
    update_book(book_id, title, book_type, status, total_chapters, last_chapter, grade, priority, link, notes)
    # Redirect back to the main page
    return redirect(url_for('index'))

def update_book(book_id, title, book_type, status, total_chapters, last_chapter, grade, priority, link, notes):
    book = Book.query.filter_by(id=book_id).first()
    if book:
        # Update the fields with the new values
        book.title = title
        book.book_type = BookType.query.filter_by(name=book_type).first()
        book.status = Status.query.filter_by(name=status).first()
        book.total_chapters = int(total_chapters)
        book.last_chapter = last_chapter
        book.grade = grade
        book.priority = priority
        book.link = link
        book.notes = notes
        # Commit the changes to the database
        db.session.commit()
        return 'Record updated successfully!'
    else:
        return 'Record not found'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

#TODO: Add sorting functionality
#TODO: Add filtering functionality
#TODO: Change the way the data is displayed
#TODO: Add buttons near each book to edit and delete it