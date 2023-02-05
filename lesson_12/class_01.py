from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from lesson_12.models import Base, User, Address, Profile, Purchase, Product

DB_USER = "andreas" # вставить свои данные
DB_PASSWORD = "andreas"
DB_NAME = "andreas"
DB_ECHO = True



if __name__ == "__main__":
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}")
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(email="test_00@test.com", password="123456")
    user = User(email="test_11@test.com", password="654321")
    user = User(email="test_22@test.com", password="987654")
    user = User(email="test_33@test.com", password="456789")
    user = User(email="test_44@test.com", password="135792")
    session.add(user)

    address = Address(user_id=user.id, city="Minsk", address="Test")
    session.add(address)

    profile = Profile(user_id=user.id, phone="+375298992123", age=20)
    session.add(profile)

    purchase = Purchase(user_id=user.id, product_id=product.id, count=1500)
    session.add(purchase)

    product = Product(user_id=user.id, name="мебель", price=500)
    session.add(product)

    session.commit()

    user = session.query(User).filter(User.email == "test@test.com").first()
    user.password = "new_password"
    session.add(user)
    session.commit()

    user = session.query(Product).filter_by(user_id=user.id).first()
    user_id = user.id
    session.add(product)
    session.commit()

    result = session.query(Profile).filter(Profile.age >= 15)
    for x in result:
        print(x)

    result = session.query(purchase).filter(purchase.count >= 1000)
    for x in result:
        print(x)
