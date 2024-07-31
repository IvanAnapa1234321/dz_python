
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
    category_list = Category.query.all()
    posts = Post.query.filter_by(category_id=category_id).order_by(Post.id.desc()).all()
    return render_template('category.html', category=blog, posts=posts ,categorys=category_list)



@app.route('/category/new', methods=['GET', 'POST'])

def new_category():
    if request.method == 'POST':
        title = request.form['title']
        category = Category(title=title)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('category'))
    category_list = Category.query.all()
    return render_template('new_category.html',categorys=category_list)



@app.route('/category/edit/<int:category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == 'POST':
        category.title=request.form['title']
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('category'))
    category_list = Category.query.all()
    return render_template('edit_category.html',  category=category,categorys=category_list)



@app.route('/category/delete/<int:category_id>', methods=['GET', 'POST'])

def delete_category(category_id: int):
    category = Category.query.get_or_404(category_id)
    if request.method == 'POST':
      db.session.delete(category)
      db.session.commit()
      return redirect(url_for('category'))
    category_list = Category.query.all()
    return render_template('delete_category.html',category=category,categorys=category_list)  

 
@app.route('/static')
def get_static(path: str):
    return send_from_directory('static',path)


@app.route('/post')
def post():
    category_list = Category.query.all()
    post_list = Post.query.all()
    return render_template('posts.html',posts=post_list,categorys=category_list)



@app.route('/post/<int:post_id>')
def post2(post_id):
    category_list = Category.query.all()
    blog = Post.query.get_or_404(post_id)
    category = Category.query.get_or_404(blog.category_id)
    return render_template('post.html', post=blog, category=category,categorys=category_list)



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
    return render_template('new_post.html', categorys=category_list)



@app.route('/post/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    edit_blog=Post.query.get_or_404(post_id)
    category = Category.query.get_or_404(edit_blog.category_id)
    if request.method == 'POST':
        post.title=request.form['title']
        post.content=request.form['content']
        category.title=request.form['title']
        post1 = Post(title=post.title,  title=category.title, content=post.content)
        db.session.add(edit_blog,category,post1=post1 )
        db.session.commit()
        return redirect(url_for('post'))
    category_list = Category.query.all()
    return render_template('edit_post.html', post=post,category=category,categorys=category_list)  




@app.route('/post/delete/<int:post_id>', methods=['GET','POST'])
def delete_post(post_id: int):
    blog = Post.query.get_or_404(post_id)
    if request.method == 'POST':
      db.session.delete(blog)
      db.session.commit()
      return redirect(url_for('post'))
    category_list = Category.query.all()
    return render_template('delete_post.html',blog=blog,categorys=category_list) 
 
 


if __name__ == '__main__':
    app.run(debug=True)


   
   
   
   
   
   
   
   
   
   
    # @app.route('/')
# def hello():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run()