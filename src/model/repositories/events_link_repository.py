import random
from src.model.configs.connection import DBConnectionHandler
from src.model.entities.events_link import EventsLink
from .interfaces.events_link_repository import EventsLinkRepositoryInterface

class EventsLinkRepository(EventsLinkRepositoryInterface):
  def insert(self, event_id: int, subscriber_id: int) -> None:
    with DBConnectionHandler() as db:
      try:
        link_final = ''.join(random.choices('0123456789', k=7))
        formatted_link = f'event-{event_id}-{subscriber_id}-{link_final}'

        new_events_link = EventsLink(
          event_id=event_id,
          subscriber_id=subscriber_id,
          link=formatted_link
        )

        db.session.add(new_events_link)
        db.session.commit()

        return formatted_link
      except Exception as exception:
        db.session.rollback()
        raise exception

  def select_events_link(self, event_id: int, subscriber_id: int) -> EventsLink:
    with DBConnectionHandler() as db:
      data = (
        db.session
        .query(EventsLink)
        .filter(
          EventsLink.event_id == event_id,
          EventsLink.subscriber_id == subscriber_id
        )
        .one_or_none()
      )

      return data