from sqlalchemy.orm import Mapped
from datetime import datetime
from .. import Base


class Purchase(Base):
    __tablename__ = "purchases"
    carrots: Mapped[int]
    pickles: Mapped[int]
    melons: Mapped[int]
    cost: Mapped[int]
    date: Mapped[datetime]