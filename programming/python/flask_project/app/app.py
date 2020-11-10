from flask import Flask, redirect, url_for
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView
from flask_login import LoginManager, current_user
from flaskext.markdown import Markdown
from flask_ckeditor import CKEditor
from flask_sessionstore import Session
from flask_session_captcha import FlaskSessionCaptcha


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
markdown = Markdown(app)
ckeditor = CKEditor(app)
Session(app)
captcha = FlaskSessionCaptcha(app)

from models import Post, User, Tag, SetSkill, UserProfile, Comment


class AdminView(ModelView):
    def is_accessible(self):
        admin_user = current_user.get_id()
        if admin_user == '1':
            return current_user

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('index'))


class HomeAdminView(AdminIndexView):
    def is_accessible(self):
        admin_user = current_user.get_id()
        if admin_user == '1':
            return current_user

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('index'))


admin = Admin(app, 'timl.admin', url='/', index_view=HomeAdminView(name='home'))
admin.add_view(AdminView(Post, db.session))
admin.add_view(AdminView(Tag, db.session))
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(UserProfile, db.session))
admin.add_view(AdminView(SetSkill, db.session))
admin.add_view(AdminView(Comment, db.session))
