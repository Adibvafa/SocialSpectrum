from flask import Blueprint, render_template, request

comm_bp = Blueprint('comm', __name__)


@comm_bp.route('/')
def index():
    return render_template('index.html')


@comm_bp.route('/comm_lesson', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    output = "Welcome to lesson..."
    return output


@comm_bp.route('/comm_quiz', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    output = "Question!"
    return output
