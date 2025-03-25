from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class EventsLink(Base):
  __tablename__ = 'Events_link'

  id = Column(Integer, primary_key=True, autoincrement=True)
  event_id = Column(Integer, ForeignKey('Events.id'))
  subscriber_id = Column(Integer, ForeignKey('Subscribers.id'))
  link = Column(String, nullable=False)




