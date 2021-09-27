from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql 


db = SQLAlchemy()
migrate = Migrate()


def create_app():

    app = Flask(__name__, static_folder='./static/')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://proj:3333@localhost/S3DB'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)


    from my_app.routes import main_route, user_route, trip_route
    app.register_blueprint(main_route.bp)
    app.register_blueprint(user_route.bp)
    app.register_blueprint(trip_route.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)