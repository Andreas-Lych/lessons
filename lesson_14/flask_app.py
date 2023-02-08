import logging

from flask import Flask, request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        logger.info("обрабатываем POST запрос")
        return request.form.to_dict()

    logger.info("обрабатываем GET запрос")
    return request.args.to_dict() # через кавычки выводит текст в эксплорер


if __name__ == "__main__":
    app.run()
