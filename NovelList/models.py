from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Book(db.Model):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    book_type_id = Column(Integer, ForeignKey('book_types.id'), nullable=False)
    book_type = relationship('BookType', backref='books')
    position = Column(Integer, nullable=False)
    last_chapter = Column(String(255), nullable=False)
    total_chapters = Column(Integer, nullable=False)
    frequency = Column(String(255))
    status_id = Column(Integer, ForeignKey('statuses.id'), nullable=False)
    status = relationship('Status', backref='books')
    notes = Column(String(255))
    priority = Column(Integer, nullable=False)
    date_added = Column(DateTime, default=datetime.utcnow().date())

class BookType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)