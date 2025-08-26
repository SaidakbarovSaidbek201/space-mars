from extension import db
from datetime import datetime

class Oquvchi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    coins = db.Column(db.Integer, default=0)
    quvvat = db.Column(db.Integer, default=100)
    course = db.Column(db.ForeignKey('course.id'), nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'
    
    
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
    
class Eduverse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return f'<Eduverse {self.name}>'
    
class VideoContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(300), nullable=False)
    eduverse = db.Column(db.ForeignKey('eduverse.id'), nullable=False)

    def __repr__(self):
        return f'<VideoContent {self.title}>'
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    photo_url = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return f'<Product {self.name}>'