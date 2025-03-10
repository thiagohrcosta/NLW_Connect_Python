import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip('Insert in DB')
def test_insert():
  subscriber_info = {
    'name': 'myName',
    'email': 'myname@email.com',
    'event_id': 2
  }

  subs_repo = SubscribersRepository()
  subs_repo.insert(subscriber_info)

@pytest.mark.skip('Select in DB')
def test_select_subscriber():
  email = 'myname@email.com'
  event_id = 2

  subs_repo = SubscribersRepository()
  resp = subs_repo.select_subscriber(email, event_id)
  print(resp.name)