from abc import ABC, abstractmethod
from src.model.entities.events import Events

class EventsRepositoryInterface(ABC):

  @abstractmethod
  def insert(self, event_name: str) -> None:
    pass

  @abstractmethod
  def select_event(self, event_name: str) -> Events:
    pass