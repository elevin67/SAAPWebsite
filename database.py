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

    def create(self, name, email, interests):
        person = self.model(name, email, interests, False)
        self.db.session.add(person)
        self.db.session.commit()

    def update(self, id, name, email, interests, contacted):
        person = self.get(id)
        person.name = name
        person.email = email
        person.interests = interests
        person.contacted = contacted
        self.db.session.commit()

    def contacted(self, id):
        person = self.get(id)
        person.contacted = True
        self.db.session.commit()

    def delete(self, id):
        person = self.get(id)
        self.db.session.delete(person)
        self.db.session.commit()

def personFactory(db):
    class Person(db.Model):
        __tablename__ = 'persons'
        id = db.Column('person_id', db.Integer, primary_key=True)
        name = db.Column(db.String(100))
        email = db.Column(db.String(100))
        interests = db.Column(db.String)
        contacted = db.Column(db.Boolean)

        def __init__(self, name, email, interests, contacted):
            self.name = name
            self.email = email
            self.interests = interests
            self.contacted = contacted
    return Person
