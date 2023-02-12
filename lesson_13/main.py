import logging

from utils import create_tables
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from lesson_13.models import Base, User, Address, Profile, Purchase, Product


DB_USER = "andreas"
DB_PASSWORD = "andreas"
DB_NAME = "andreas_1"

def create_user(session, email, password):
    user = User(email=email, password=password)
    session.add(user)
    session.commit()
    return user

def search_users(session, email):
    session.query(User).filter_by(email=email).first()
    session.find(user)
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

def create_profile(session, phone, age):
    profile = Profile(phone=phone, age=age)
    session.add(profile)
    session.commit()
    return profile

def create_purchase(session, user_id, product_id, count):
    purchase = Purchase(user_id=user_id, product_id=product_id, count=count)
    session.add(purchase)
    session.commit()
    return purchase


if __name__ == "__main__":
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"
    )
    if not database_exists(engine.url):
        create_database(engine.url)

    session = create_tables(engine)

    menu = """
    1. создать пользователя
    2. найти пользователя
    3. выйти
    """
    buy = """
     спасибо что выбрали нас. До новых встреч
     """

    while True: # задает функцию бесконечности, пока выбор не выпадет на цифру 3 выход
        logger.info(menu)
        choice = input("выберите действие")

        if choice == "1":
            email = input ("введите email")
            password = input ("введите пароль")
            city = input ("введите город")
            address = input ("ввести адрес")
            phone = input ("ввести телефон")
            age = input ("ввести возраст")

            user = create_user(session, email, password)
            address = create_address(session, city, address)
            profile = create_profile(session, phone, age)
            logger.info(f"User #{user.id} is created")

        elif choice == "3":
            logger.info(buy)
            exit()