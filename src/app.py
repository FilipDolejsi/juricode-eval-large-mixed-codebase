"""Generic Flask app scaffold — boilerplate, no business logic yet."""

from flask import Flask

from src.routes.health import health_bp
from src.utils.logger import get_logger

logger = get_logger(__name__)


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    logger.info("app created")
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
