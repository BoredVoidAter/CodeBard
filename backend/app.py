from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from .models import db, Story, CodeLine
from .api_routes import api_bp
from .interpreter import interpret_story

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(api_bp, url_prefix='/api')

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return render_template('story_view.html')

    @app.route('/story/<int:story_id>')
    def story_view(story_id):
        story = Story.query.get_or_404(story_id)
        code_lines = CodeLine.query.filter_by(story_id=story_id).order_by(CodeLine.id).all()
        narrative = interpret_story(code_lines)
        return render_template('story_view.html', story=story, code_lines=code_lines, narrative=narrative)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
