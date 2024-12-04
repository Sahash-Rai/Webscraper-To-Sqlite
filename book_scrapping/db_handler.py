from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///books.db"

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    title = Column(String, primary_key=True)
    price = Column(String)
    url = Column(String)

def create_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

def store_books_in_db(books):
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for book in books:
        new_book = Book(title=book['title'], price=book['price'], url=book['url'])
        session.add(new_book)
    
    session.commit()
    session.close()
