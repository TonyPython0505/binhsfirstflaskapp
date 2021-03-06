from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from genesis import db

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(100), index = True, unique = True)
  email = db.Column(db.String(100), index = True, unique = True)
  password_hash = db.Column(db.String(100), index = True, unique = False)
  posts = db.relationship('Post', backref = "author", lazy = "dynamic", cascade = "all, delete, delete-orphan")

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password_hash(self, password):
    return check_password_hash(self.password_hash, password)
  
  def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(140))
    country = db.Column(db.String(140))
    description = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.description)