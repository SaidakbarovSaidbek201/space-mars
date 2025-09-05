from flask import Flask, render_template, request, redirect, url_for, session, g
from extension import db
import os
from functools import wraps
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView

# Flask app
app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.secret_key = 'n9$2@!Df6wE^zXoB7rL0#QsA3!vUz1gT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# import models
from models import Oquvchi, Course, Category, Eduverse, VideoContent, Product

# from flask_admin.contrib.sqla import ModelView

# class EduverseAdmin(ModelView):
#     form_columns = ['name', 'description', 'category', 'video']  # укажем поля

# # Flask-Admin
# admin = Admin(app, name='My Admin Panel', template_mode='bootstrap4')
# admin.add_view(ModelView(Oquvchi, db.session))
# admin.add_view(ModelView(Course, db.session))
# admin.add_view(ModelView(Category, db.session))
# admin.add_view(ModelView(VideoContent, db.session))
# admin.add_view(EduverseAdmin(Eduverse, db.session))  # кастомная админка
# admin.add_view(ModelView(Product, db.session))



# ---- Авторизация ----
def login_required(view_fn):
    @wraps(view_fn)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return view_fn(*args, **kwargs)
    return wrapper


@app.before_request
def load_current_user():
    g.current_user = None
    uid = session.get('user_id')
    if uid:
        g.current_user = Oquvchi.query.get(uid)


@app.route('/')
@login_required
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    err = None
    if request.method == 'POST':
        username = request.form.get("modme_id")
        password = request.form.get("parol")

        print(">>> FORM:", username, password)   # 👈 DEBUG
        user = Oquvchi.query.filter_by(username=username, password=password).first()
        print(">>> USER:", user)                 # 👈 DEBUG

        if user:
            session['user_id'] = user.id
            return redirect(url_for('home'))
        else:
            err = "Parol yoki login noto‘g‘ri!"

    return render_template('login.html', err=err)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


# ---- Остальные страницы ----
@app.route('/courses')
@login_required
def courses():
    user = g.current_user
    user_courses = user.courses if user else []
    return render_template('courses.html', courses=user_courses)


@app.route('/eduverse')
@login_required
def eduverse():
    eduverses = Eduverse.query.all()
    categories = Category.query.all()
    return render_template('eduverse.html', eduverses=eduverses, categories=categories)


@app.route('/marscode')
@login_required
def marscode():
    return render_template('marscode.html')


@app.route('/blog')
@login_required
def blog():
    return render_template('blog.html')


@app.route('/shop')
@login_required
def shop():
    products = Product.query.all()
    return render_template('shop.html', products=products)


# app.py

if __name__ == '__main__':
    app.run(debug=True)

# всегда при запуске (и на Render, и локально) создаст таблицы
with app.app_context():
    db.create_all()
