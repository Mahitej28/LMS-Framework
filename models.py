from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="Mahima",
    host="localhost",
    database="zaltan",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)


Base.metadata.create_all(engine)



