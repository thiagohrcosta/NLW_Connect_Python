from abc import ABC, abstractmethod
from src.model.entities.subscribers import Subscribers

class SubscribersRepositoryInterface(ABC):

  @abstractmethod
  def insert(self, subscriber_infos: dict) -> None:
   pass

  @abstractmethod
  def select_subscriber(self, email: str, event_id: int) -> Subscribers:
   pass