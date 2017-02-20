from punchstarter import db

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    projects = db.relationship('Project', backref='creator', foreing_key='Project.id')
    pledges = db.relationship('Pledge', backref='pledger', foreing_key='Pledge.member_id')

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id') nullable=False)

    name = db.Column(db.String(100))
    short_description = db.Column(db.Text)
    long_description = db.Column(db.Text)
    goal_amount = db.Column(db.Integer)
    time_start = db.Column(db.DateTime)
    time_end = db.Column(db.DateTime)
    time_created = db.Column(db.DateTime)
    pledges = db.relationship('Pledge', backref='project', foreing_key='Pledge.project_id')


class Pledge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id') nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id') nullable=False)
    amount = db.Column(db.Integer)
    time_created = db.Column(db.DateTime)
