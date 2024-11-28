from flask import Blueprint

# Create a blueprint for your routes
bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return 'Hello from the index page!'

@bp.route('/about')
def about():
    return 'This is the about page.'