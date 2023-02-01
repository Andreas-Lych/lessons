from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from lesson_12.models import Base, User, Address, Profile

DB_USER = "manti" # вставить свои данные
DB_PASSWORD = "manti"
DB_NAME = "manti"
DB_ECHO = True



if __name__ == "__main__":
    engine = create_engine(f"postgresql://andreas:andreas@localhost/andreas")
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(email="test@test.com", password="password")
    session.add(user)

    address = Address(user_id=user.id, city="Minsk", address="Test")
    session.add(address)

    profile = Profile(user_id=user.id, phone="+375298992123", age=20)
    session.add(profile)

    session.commit()

    user = session.query(User).filter(User.email == "test@test.com").first()
    user.password = "new_password"
    session.add(user)
    session.commit()

    result = session.query(Profile).filter(Profile.age >= 15)
    for x in result:
        print(x)
