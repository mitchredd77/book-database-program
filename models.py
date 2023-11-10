from sqlalchemy import (create_engine, Column, 
                        Integer, String, Date)
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///books.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column('Title', String)
    author = Column('Author', String)
    published_date = Column('Published Date', Date)
    price = Column('Price', Integer)

    def __repr__(self):
        return f'Title: {self.title}, Author: {self.author}, Published Date: {self.published_date}, Price: {self.price}'
# books.db
# create a model
# title, author, date published, price
