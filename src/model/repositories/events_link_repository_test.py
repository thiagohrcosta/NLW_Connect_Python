import pytest
from .events_link_repository import EventsLinkRepository

@pytest.mark.skip('Insert in DB')
def test_insert_events_link():
  event_id = 121
  subs_id = 181
  event_link_repo = EventsLinkRepository()

  event_link_repo.insert(event_id, subs_id)