from flask import Blueprint
from flask import render_template
from models import SetSkill

skill_page = Blueprint('skill', __name__, template_folder='templates')


@skill_page.route('/')
def index():
    skills = SetSkill.query.all()
    return render_template('skill/index.html', skills=skills)
