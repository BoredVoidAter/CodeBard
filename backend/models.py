from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    code_lines = db.relationship('CodeLine', backref='story', lazy=True)

    def __repr__(self):
        return f'<Story {self.title}>'

class CodeLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), nullable=False)
    line_number = db.Column(db.Integer, nullable=False)
    code = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<CodeLine {self.line_number}: {self.code}>'
