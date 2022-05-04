from instances.db import db


class Book(db.Model):
    __tablename__ = "books"
    id_ = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    author = db.Column(db.String(120))

    def to_json(self):
        return {"id": self.id_, **vars(self)}


    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by(cls, id_:int):
        return cls.query.filter_by(id_=id_).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

#  The update method still need to be made ......
        
