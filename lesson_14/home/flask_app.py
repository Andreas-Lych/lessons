import logging

from lesson_13.models import Base, User
from flask import Flask, request

DB_USER = "andreas"
DB_PASSWORD = "andreas"
DB_NAME = "andreas_1"

def create_user(session, email, password):
    user = User(email=email, password=password)
    session.add(user)
    session.commit()
    return user

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    if request.method == "POST":
        logger.info("обрабатываем POST запрос")
        return request.form.to_dict()

    for key, item in request.args.to_dict().items():  # надо вернуть ключ занчение парами
        logger.info(f"{key}={item}")

    logger.info("обрабатываем GET запрос")
    return request.args.to_dict() # через кавычки выводит текст в эксплорер

if __name__ == "__main__":
    app.run()
