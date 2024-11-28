from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .db import db
from app.routes import bp

app = Flask(__name__)

app.config.from_object('config.Config')
app.register_blueprint(bp)

db.init_app(app)
migrate = Migrate(app, db)
