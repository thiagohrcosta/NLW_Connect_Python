from sqlalchemy import func, desc
from src.model.configs.connection import DBConnectionHandler
from src.model.entities.subscribers import Subscribers
from .interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscribersRepository(SubscribersRepositoryInterface):
  def insert(self, subscriber_infos: dict) -> None:
    with DBConnectionHandler() as db:
      try:
        new_subscriber = Subscribers(
          name=subscriber_infos.get('name'),
          email=subscriber_infos.get('email'),
          event_id=subscriber_infos.get('event_id'),
        )
        db.session.add(new_subscriber)
        db.session.commit()
      except Exception as exception:
        db.session.rollback()
        raise exception

  def select_subscriber(self, email: str, event_id: int) -> Subscribers:
    with DBConnectionHandler() as db:
      data = (
        db.session
        .query(Subscribers)
        .filter(
          Subscribers.email == email,
          Subscribers.event_id == event_id
        )
        .one_or_none()
      )

      return data

  def select_subscribers_by_link(self, link: str, event_id: int) -> list:
    with DBConnectionHandler() as db:
      data = (
        db.session
        .query(Subscribers)
        .filter(
          Subscribers.link == link,
          Subscribers.event_id == event_id
        )
        .all()
      )

      return data

  def get_ranking(self, event_id: int) -> list:
    with DBConnectionHandler() as db:
      result = (
        db.session
        .query(
          Subscribers.link,
          func.count(Subscribers.id).label('total')
        )
        .filter(
          Subscribers.event_id == event_id,
          Subscribers.link.isnot(None)
        )
        .group_by(Subscribers.link)
        .order_by(desc('total'))
        .all()
      )

      return result


