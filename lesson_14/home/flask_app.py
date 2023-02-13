import logging

from flask import Flask, request

from sqlalchemy import create_engine
from lesson_13.utils import create_tables
from lesson_13.models import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_USER = "andreas"
DB_PASSWORD = "andreas"
DB_NAME = "andreas_1"

def create_user(session, email, password):
    user = User(email=email, password=password)
    session.add(user)
    session.commit()
    return user

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        create_user(app.session, request.form.to_dict()['email'],request.form.to_dict()['password'],)
        logger.info("Обрабатываю POST запрос")
        return request.form.to_dict()

    logger.info("Обрабатываю GET запрос")
    return request.args.to_dict()


if __name__ == "__main__":
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"
    )

    app.session = create_tables(engine)

    app.run()