import os

from flask import Flask

from app.web.student_routes import student_bp


def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )

    app.config["SECRET_KEY"] = os.environ.get(
        "COSS_SECRET_KEY",
        "dev-only-change-this-key",
    )

    app.register_blueprint(student_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)