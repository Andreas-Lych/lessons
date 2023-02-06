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

    while True: # задает функцию бесконечности, пока выбор не выпадет на цифру 3 выход
        logger.info(menu)
        choice = input("выберите действие")

        if choice == "1":
            email = input ("введите email")
            password = input ("введите пароль")

            user = create_user(session, email, password)
            logger.info(f"User #{user.id} is created")

        elif choice == "3":
            exit()