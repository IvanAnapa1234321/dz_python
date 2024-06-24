
from flask import Flask, render_template, request, redirect, url_for
from models import Category, db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///category.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/qwerty')
def qwerty(): 
    return render_template('qwerty.html')

@app.route('/category')
def category():
    category_list = Category.query.all()
    return render_template('categorys.html',categorys=category_list)
@app.route('/category/<int:category_id>')
def blog_post(category_id,id):
    blog = Category.query.get_or_404(category_id)
    if request.method == 'POST':
        category.id = request.form['id']
        category.parent_id= request.form['parent_id']
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('categorys.html', category=blog)

 

 


if __name__ == '__main__':
    app.run(debug=True)


   
   
   
   
   
   
   
   
   
   
    # @app.route('/')
# def hello():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run()