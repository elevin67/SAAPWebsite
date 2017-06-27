from flask_sqlalchemy import SQLAlchemy

class Database:
    def __init__(self, app):
        db = SQLAlchemy(app)
        self.db = db
        self.model = personFactory(db)

    def get(self, id=None):
        if id:
            return self.model.query.get(id)
        return self.model.query.all()

    def create(self, fname, lname, email, interests):
        person = self.model(fname, lname, email, interests, False)
        self.db.session.add(person)
        self.db.session.commit()

    def update(self, id, fname, lname, email, interests, called):
        person = self.get(id)
        person.fname = fname
        person.lname = lname
        person.email = email
        person.interests = interests
        person.called = called
        self.db.session.commit()

    def called(self, id):
        person = self.get(id)
        person.called = True
        self.db.session.commit()

    def delete(self, id):
        person = self.get(id)
        self.db.session.delete(person)
        self.db.session.commit()

def personFactory(db):
    class Person(db.Model):
        __tablename__ = 'persons'
        id = db.Column('person_id', db.Integer, primary_key=True)
        fname = db.Column(db.String(20))
        lname = db.Column(db.String(20))
        email = db.Column(db.String(100))
        interests = db.Column(db.String)
        called = db.Column(db.Boolean)

        def __init__(self, fname, lname, email, interests, called):
            self.fname = fname
            self.lname = lname
            self.email = email
            self.interests = interests
            self.called = called
    return Person
