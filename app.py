from flask import Flask, render_template

from config import Config
from extensions import db
from routes.contact_routes import contact_bp


def create_app(config_class=Config):

    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

    app.register_blueprint(contact_bp)

    @app.route("/")
    def home():

        return render_template("index.html")

    return app


app = create_app()


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )