from flask import Flask, render_template, request
from extension import db
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.secret_key = 'n9$2@!Df6wE^zXoB7rL0#QsA3!vUz1gT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'blog.db')

# инициализируем базу
db.init_app(app)

# импорт моделей только после db.init_app
from models import Oquvchi, Course, Category, Eduverse, VideoContent, Product


@app.route('/')
def home():

    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    err = None
    if request.method == 'POST':
        modme_id = request.form.get("modme_id")
        parol = request.form.get("parol")

        # Oddiy tekshiruv
        if modme_id == "12345" and parol == "123456":
            return render_template('index.html')
        else:
            err = "Parol noto'g'ri!"

    return render_template('login.html', err=err)


@app.route('/courses')
def courses():
    # courses = Course.query.all()
    return render_template('courses.html')

@app.route('/eduverse')
def eduverse():
    # eduverses = Eduverse.query.all()    
    return render_template('eduverse.html')

@app.route('/marscode')
def marscode():
    return render_template('marscode.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')


if __name__ == '__main__':
    app.run(debug=True)
