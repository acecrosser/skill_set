from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
import datetime
import re
from flask_login import UserMixin


def slug_fly(string):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', string)


post_tags = db.Table('posts_tags',
                     db.Column('post_id', db.Integer(), db.ForeignKey('post.id')),
                     db.Column('tag_id', db.Integer(), db.ForeignKey('tag.id'))
                     )

post_comments = db.Table('post_comments',
                         db.Column('post_id', db.Integer(), db.ForeignKey('post.id')),
                         db.Column('comment_id', db.Integer(), db.ForeignKey('comment.id'))
                         )


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'User, id: {self.id}, username: {self.username}'


class UserProfile(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    full_name = db.Column(db.String(250), default='empty')
    date_of_birth = db.Column(db.Date(), default=datetime.datetime.utcnow())
    telegram = db.Column(db.String(150))
    number = db.Column(db.String(20))
    about_me = db.Column(db.Text())
    education = db.Column(db.String(255))
    languages = db.Column(db.String(140))
    experience = db.Column(db.Text())
    links = db.Column(db.String(250))
    contacts = db.Column(db.Text())

    def get_age(self):
        today = datetime.datetime.today()
        return today.year - self.date_of_birth.year - \
            ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(155))
    slug = db.Column(db.String(155))
    body = db.Column(db.Text())
    create = db.Column(db.DateTime(), index=True, default=datetime.datetime.utcnow())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    # связь между моделями Пост и Тег, где обратная ссылка (для модели Тега) именуется (бекреф) постс
    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))
    comments = db.relationship('Comment', secondary=post_comments, backref=db.backref('posts', lazy='dynamic'))

    def generate_slug(self):
        if self.title:
            self.slug = slug_fly(self.title).lower()

    def __repr__(self):
        return f'{self.title}'


class Tag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slug_fly(self.name).lower()

    def __repr__(self):
        return f'{self.name}'


class SetSkill(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    soft = db.Column(db.String(250))
    hard = db.Column(db.String(250))
    other = db.Column(db.String(250))
    books = db.Column(db.String(250))
    in_progress = db.Column(db.String(250))

    def __repr__(self):
        return 'class skill soft'


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(150))
    body = db.Column(db.Text())
    date_time = db.Column(db.DateTime(), default=datetime.datetime.utcnow())

    def __init__(self, *args, **kwargs):
        super(Comment, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'{self.id}'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
