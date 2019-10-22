from . import db

#...

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String())
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

       
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User{self.name}'

class Pitch(db.Model):
    __tablename__ ='pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    category = db.Column(db.String(255), nullable=False)