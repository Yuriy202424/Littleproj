from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, DeclarativeBase
from sqlalchemy import create_engine



engine = create_engine("sqlite:///my_db.db", echo=True)
Session = sessionmaker(engine)


class Base(DeclarativeBase):
    id: Mapped [int]= mapped_column(primary_key=True)

def up():
    Base.metadata.create_all(engine)


def down():
    Base.metadata.drop_all(engine)



from .models import Purchase, User, Nick


up()