from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Followers(Base):
    __tablename__ = "followers"

    id = Column('id', Integer, primary_key=True)
    follower_name = Column('follower_name', String, unique=False)
    follow_at_name = Column('follow_at_name', String, unique=False)
    effected_by_bot = Column('effected_by_bot', Boolean, default=False)

    def __str__(self):
        return self.follower_name


class Targets(Base):
    __tablename__ = "targets"

    id = Column('id', Integer, primary_key=True)
    target_name = Column('target_name', String)
    target_followed_date = Column('target_followed_date', Date)  # when we start to follow at the target
    shooter_name = Column('shooter_name', String)
    story_watched = Column('story_watched', Boolean, default=False)


engine = create_engine('sqlite:///ig_bot.db', echo=True)
#Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)
session = Session()








