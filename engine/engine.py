from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from scrap import scrape_youtube


# Define the database URL
DATABASE_URL = "sqlite:///youtube_data.db"  # Using SQLite for simplicity

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Define the base class for declarative class definitions
Base = declarative_base()

# Extend the model to include a transcript field
class Video(Base):
    __tablename__ = 'videos'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    link = Column(String, nullable=False)
    channel_name = Column(String, nullable=False)
    channel_link = Column(String, nullable=False)
    views = Column(String, nullable=False)
    upload_date = Column(String, nullable=False)
    transcript = Column(Text, nullable=True)  # Added transcript field

# Create the table
Base.metadata.create_all(engine)

# Create a session factory
SessionLocal = sessionmaker(bind=engine)


def add_video(title, link, channel_name, channel_link, views, upload_date):
    for video in data:
        new_video = Video(
        title=video["title"],
        link=video["link"],
        channel_name=video["channel_name"],
        channel_link=video["channel_link"],
        views=video["views"],
        upload_date=video["upload_date"]
        )
        session.add(new_video)
        session.commit()


session.close()