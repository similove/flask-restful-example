from sqlalchemy import Column, Integer, String

from src.db.database import Base


class User(Base):
    __tablename__ = 'user'
    user_id = Column('user_id', Integer, primary_key=True)
    name = Column(String(60))
    password = Column(String(60))
    email = Column(String(60))

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return '{user_id:%r name:%r password:%r email:%r}' \
               % (self.user_id, self.name, self.password, self.email)
