from app import app
import view, errors
from app import db, migrate
from posts.routes_blog import posts
from skill.skill_view import skill_page
from profile.profile_view import profile_page


app.register_blueprint(posts, url_prefix='/portfolio')
app.register_blueprint(skill_page, url_prefix='/skillset')
app.register_blueprint(profile_page, url_prefix='/profile')


if __name__ == '__main__':
    app.run()

