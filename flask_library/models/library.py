from . import db  # now db is already defined in __init__.py

class Library(db.Model):
    __tablename__ = 'library'

    isbn = db.Column(db.String(13), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author
        }
