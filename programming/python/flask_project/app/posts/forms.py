from flask_wtf import FlaskForm
from wtforms import StringField
from flask_ckeditor import CKEditorField


class PostFrom(FlaskForm):
    title = StringField('Заголовок')
    body = CKEditorField('body')
    tags = StringField('Основной тег')


class CommentForm(FlaskForm):
    username = StringField('Ваше имя')
    body = StringField('Комментарий')
