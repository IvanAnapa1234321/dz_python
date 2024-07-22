
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
def new_category():
    if request.method == 'POST':
        title = request.form['title']
        category = Category(title=title)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('new_category.html')

@app.route('/edit/<int:category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == 'POST':
        category.title=request.form['title']
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('edit_category.html',  category=category)

@app.route('/delete/<int:category_id>', methods=['GET', 'POST'])

def delete_category(category_id: int):
    category = Category.query.get_or_404(category_id)
    if request.method == 'POST':
   
      db.session.delete(category)
      db.session.commit()
      return redirect(url_for('category'))
    return render_template('delete_category.html',category=category)  

 
@app.route('/static')
def get_static(path: str):
    return send_from_directory('static',path)

@app.route('/post/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        category_id = request.form['category_id']
        content = request.form['content']
        post = Post(title=title,category_id=category_id, content=content)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('post'))
    category_list = Category.query.all()
    return render_template('new_post.html', categorys=category_list,)

@app.route('/post')
def post():
    post_list = Post.query.all()
    return render_template('posts.html',posts=post_list)


@app.route('/post/<int:post_id>')
def post2(post_id):
    blog = Post.query.get_or_404(post_id)
    blog1 = Category.query.get_or_404(blog.category_id)
    return render_template('post.html', post=blog, category=blog1)


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id: int):
    if request.method == 'POST':
      blog = Post.query.get_or_404(post_id)
      db.session.delete(post_id)
      db.session.commit()
      return redirect(url_for('post'))
    return render_template('delete_post.html',blog=blog)  
 


if __name__ == '__main__':
    app.run(debug=True)


   
   
   
   
   
   
   
   
   
   
    # @app.route('/')
# def hello():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run()