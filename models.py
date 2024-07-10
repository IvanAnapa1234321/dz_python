from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    parent_id=db.Column(db.Integer)
    title=db.Column(db.String(200),nullable=False)
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(300),nullable=False)
    content = db.Column(db.Text, nullable=False)