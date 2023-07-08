from flask import Flask
from website.routes import chat_bp

app = Flask(__name__)



app.register_blueprint(chat_bp)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=81)
