from app import db
from werkzeug.security import check_password_hash as cph
from werkzeug.security import generate_password_hash as gph

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def set_password(self, password):
        self.password = gph(password)
        return True
    
    def is_valid(self, password):
        return cph(self.password, password)
    
    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def create(cls, name, username, password):
        user = cls(name=name,username=username)
        user.set_password(password)
        user.save()
        user.update()
