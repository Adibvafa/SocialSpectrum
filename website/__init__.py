from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'THE CYBER SAVVY NINJAS'

    # for database
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)          # assigning the database to this application

    # defining the schema of this database is done in models.py

    # after defining blueprints, we need to register them here
    from .views import views

    # specifies a prefix that we have to put before any of the blueprint paths
    app.register_blueprint(views, url_prefix='/')

    return app
