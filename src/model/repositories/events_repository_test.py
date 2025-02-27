import pytest
from .events_repository import EventsRepository

@pytest.mark.skip('Insert in DB')
def test_insert_events():
  event_name = "EventTest"
  event_repo = EventsRepository()

  event_repo.insert(event_name)

@pytest.mark.skip('Select in DB')
def test_select_event():
  event_name = 'EventTest'
  event_repo = EventsRepository()

  event = event_repo.select_event(event_name)
  print(event.name)
