from sqlalchemy.orm import sessionmaker

from lesson_13.models import Base

def create_tables(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def get_users_by_product_id(session, product_id: int) -> list:# вариант 1
    purchaces = session.quary(Purchase).filter_by(product_id=product_id)
    user_ids = []
    for purchase in purchaces:
        user_ids.append(purchase.user_id)
    return list(set(user_ids))