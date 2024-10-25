from sqlalchemy.orm import Mapped
from .. import Base


class Nick(Base):
    __tablename__ = "nicks"
    nickname: Mapped[str]