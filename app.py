
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from models import Category, Post, db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///category.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index(): 
    return render_template('index.html')


@app.route('/category')
def category():
    category_list = Category.query.all()
    return render_template('categorys.html',categorys=category_list)
@app.route('/category/<int:category_id>')
def blog_post(category_id):
    blog = Category.query.get_or_404(category_id)
    return render_template('category.html', category=blog)

@app.route('/category/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        post = Category(title=title)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('new_category.html')

@app.route('/edit/<int:category_id>', methods=['GET', 'POST'])
def edit_post(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == 'POST':
        category.title=request.form['title']
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('edit_post.html',  category=category)

@app.route('/delete/<int:category_id>', methods=['GET', 'POST'])

def delete_post(category_id: int):
    category = Category.query.get_or_404(category_id)
    if request.method == 'POST':
   
      db.session.delete(category)
      db.session.commit()
      return redirect(url_for('category'))
    return render_template('delete_category.html',category=category)  
 
@app.route('/static')
def get_static(path: str):
    return send_from_directory('static',path)


 


if __name__ == '__main__':
    app.run(debug=True)


   
   
   
   
   
   
   
   
   
   
    # @app.route('/')
# def hello():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run()