from flask import Flask, render_template
from flask_sqlalchemy import SQLALchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

from app import app, db

app = Flask(__name__)
app.config.from_object('punchstarter.default_settings')

manager = Manager(app)

db = SQLALchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@app.route("/")
def hello():
    return render_template("index.html")
