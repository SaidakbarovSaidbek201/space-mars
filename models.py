from extension import db
from datetime import datetime

# таблица-связка
oquvchi_courses = db.Table(
    'oquvchi_courses',
    db.Column('oquvchi_id', db.Integer, db.ForeignKey('oquvchi.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
)

class Oquvchi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    coins = db.Column(db.Integer, default=0)
    quvvat = db.Column(db.Integer, default=100)

    courses = db.relationship('Course', secondary=oquvchi_courses, backref='students')

    def __repr__(self):
        return f'<User {self.username}>'

    
    def my_courses(self):
        return self.courses

        
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Course {self.title}>'
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<Category {self.name}>'


class VideoContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(300), nullable=False)

    @property
    def youtube_id(self):
        if "youtu.be/" in self.url:
            return self.url.split("/")[-1].split("?")[0]
        elif "watch?v=" in self.url:
            return self.url.split("v=")[-1].split("&")[0]
        elif "embed/" in self.url:
            return self.url.split("embed/")[-1].split("?")[0]
        return self.url

    def __repr__(self):
        return f'<VideoContent {self.title}>'

    
class Eduverse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey("video_content.id"))

    category = db.relationship('Category', backref='eduverses')
    video = db.relationship('VideoContent', backref='eduverses')
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    photo_url = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return f'<Product {self.name}>'