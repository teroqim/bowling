import pytest
from bowlingapi.scorecard import Scorecard

@pytest.fixture()
def scorecard():
    print("setup")
    yield Scorecard()
    print("teardown")

class Test_to_dict(object):
  def test_initial_score(self, scorecard):
    d = scorecard.to_dict()
    assert d['score'] == None

  def test_initial_frames(self, scorecard):
    d = scorecard.to_dict()
    assert d['frames'] == []

