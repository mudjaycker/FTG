from instances.db import db

class Book(db.Model):
    __tablename__ = "books"
    id_ = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    author = db.Column(db.String(120))

    def to_json(self):
        return {
            "id": self.id_,
            "age": self.age,
            "author": self.author
        }

    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit() 

    @classmethod
    def get_all(cls):
        return cls.query.all()