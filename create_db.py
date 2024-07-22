from flask import Flask
from models import Category, Post, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///category.db'
db.init_app(app)

def new_func():
        post1=Post(title='hnjuaeiyr',
        content='IUCBNWeicbwCWicniwCNIJNICW',
        category_id=1)
        
 
        
        db.session.add(post1)
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
        category1 = Category(
            title='Домовладения')
        category2 = Category(
            title='Аренда жилья')
        category3 = Category(
            title='Гаражи')
        
        # Сохраняем посты в БД
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.commit()

        new_func()
        