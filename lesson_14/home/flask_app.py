import logging

from flask import Flask, request

from sqlalchemy import create_engine
from lesson_13.utils import create_tables
from lesson_13.models import User, Address, Product,  Profile, Purchase, Product

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
def create_address(session, city, address):
    address = Address(city=city, address=address)
    session.add(address)
    session.commit()
    return address
def create_product(session, name, price):
    product = Product(name=name, price=price)
    session.add(product)
    session.commit()
    return product

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        create_user(app.session, request.form.to_dict()['email'],request.form.to_dict()['password'],)
        create_address(app.session, request.form.to_dict()['city'], request.form.to_dict()['address'],)
        create_product(app.session, request.form.to_dict()['name'], request.form.to_dict()['price'],)

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