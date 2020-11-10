from flask import Blueprint, render_template, redirect
from models import User, UserProfile


profile_page = Blueprint('profile', __name__, template_folder='templates')


@profile_page.route('/')
def index():
    user = User.query.filter_by(id=1).first_or_404()
    profile = UserProfile.query.filter_by(id=1).first()
    return render_template('profile/profile.html', user=user, profile=profile)
