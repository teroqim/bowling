import pytest
from bowlingapi.scorecard import Scorecard

@pytest.fixture()
def scorecard():
    print("setup")
    yield Scorecard()
    print("teardown")

class Test_to_dict__score(object):
  def test_initial_score(self, scorecard):
    d = scorecard.to_dict()
    assert d['score'] == None

  # First roll
  def test_first_roll_score(self, scorecard):
    scorecard.roll(3)
    d = scorecard.to_dict()
    assert d['score'] == 3

  # Sums up 'simple' values.
  # 'Simple' rolls means none-spare and non-strike
  def test_sums_up_simple_rolls(self, scorecard):
    scorecard.roll(2)
    scorecard.roll(5)
    scorecard.roll(9)
    scorecard.roll(0)
    scorecard.roll(4)
    d = scorecard.to_dict()
    assert d['score'] == 20

  # Spare
  def test_spare_increases_score_by_next_roll_twice(self, scorecard):
    scorecard.roll(2)
    scorecard.roll(8)

    score = scorecard.to_dict()['score']

    scorecard.roll(4)

    assert scorecard.to_dict()['score'] == (score + 8)

  # Strike second roll
  def test_strike_increases_score_by_next_roll_twice(self, scorecard):
    scorecard.roll(10)

    score = scorecard.to_dict()['score']

    scorecard.roll(4)

    assert scorecard.to_dict()['score'] == (score + 8)
  
  # Strike third roll
  def test_second_simple_roll_after_strike_increases_score_by_twice_roll_value(self, scorecard):
    scorecard.roll(10)
    scorecard.roll(4)

    score = scorecard.to_dict()['score']

    scorecard.roll(4)

    assert scorecard.to_dict()['score'] == (score + 8)

  # Strike fourth roll, no addition
  def test_third_roll_after_strike_increases_score_roll_value(self, scorecard):
    scorecard.roll(10)
    scorecard.roll(6)
    scorecard.roll(2)

    score = scorecard.to_dict()['score']

    scorecard.roll(4)

    assert scorecard.to_dict()['score'] == (score + 4)

  # TODO: If last 2 rolls where both strikes, make sure score is updated properly

  # TODO: Test full series, with only simple value

  # TODO: Test full series, with only spares

  # TODO: Test full series, with only strikes

  # TODO: Test mix of spares, simple rolls and strikes


class Test_to_dict__frames(object):
  def test_initial_frames(self, scorecard):
      d = scorecard.to_dict()
      assert d['frames'] == []

  # First roll creates frame with no second roll
  def test_first_roll_creates_frame(self, scorecard):
    scorecard.roll(3)
    assert len(scorecard.to_dict()['frames']) == 1

  def test_first_roll_created_frame_with_correct_first_value(self, scorecard):
    scorecard.roll(3)
    frame = scorecard.to_dict()['frames'][0]
    assert frame['first'] == 3

  def test_first_roll_created_frame_with_no_second_value(self, scorecard):
    scorecard.roll(3)
    frame = scorecard.to_dict()['frames'][0]
    assert frame['second'] == None

  def test_second_roll_in_frame_has_correct_value(self, scorecard):
    scorecard.roll(3)
    scorecard.roll(6)
    frame = scorecard.to_dict()['frames'][0]
    assert frame['second'] == 6

  # Roll after frame with a first non-strike roll creates second value
  def test_first_roll_after_finished_frame_with_2_rolls_creates_new_frame(self, scorecard):
    scorecard.roll(3)
    scorecard.roll(3)
    scorecard.roll(3)
    assert len(scorecard.to_dict()['frames']) == 2

  # Roll after strike, creates new frame
  def test_roll_after_strike_creates_new_frame(self, scorecard):
    # First frame
    scorecard.roll(2)
    scorecard.roll(2)

    # Strike
    scorecard.roll(10)

    # Third frame
    scorecard.roll(5)

    assert len(scorecard.to_dict()['frames']) == 3

  def test_10_strikes_10_frames(self, scorecard):
    for i in range(10):
      scorecard.roll(10)

    assert len(scorecard.to_dict()['frames']) == 10
  
  def test_20_non_strikes_10_frames(self, scorecard):
    for i in range(20):
      scorecard.roll(4)

    assert len(scorecard.to_dict()['frames']) == 10

  # TODO: Make sure first and second vals are updated correctly for spare and strikes

class Test_is_finished(object):
  def test_initial_is_finished(self, scorecard):
    assert scorecard.is_finished() == False

  # Not finished after a couple of rolls
  def test_not_finished_after_5_roll(self, scorecard):
    for i in range(5):
      scorecard.roll(5)

    assert scorecard.is_finished() == False

  def test_not_finished_before_final_roll(self, scorecard):
    for i in range(19):
      scorecard.roll(5)

    assert scorecard.is_finished() == False

  # Finished after final roll
  def test_finished_after_finished_game(self, scorecard):
    for i in range(20):
      scorecard.roll(5)

    assert scorecard.is_finished() == True # '== True' for clarity

class Test_roll(object):
  def test_roll_no_arg_exception(self, scorecard):
    with pytest.raises(TypeError):
      scorecard.roll()

  # TODO: Test arg outside boundary 0-10 exception
  def test_roll_value_below_0(self, scorecard):
    with pytest.raises(ValueError):
      scorecard.roll(-3)

  def test_roll_value_above_10(self, scorecard):
    with pytest.raises(ValueError):
      scorecard.roll(12)

  def test_roll_value_inside_boundary_no_exception(self, scorecard):
      scorecard.roll(5)

  # Second roll in frame max (10 - first_roll)
  def test_invalid_second_roll_in_frame_raise_exception(self, scorecard):
    scorecard.roll(5)
    with pytest.raises(ValueError):
      scorecard.roll(6)

  # Roll after finished game raise exception
  def test_roll_after_finished_game_rase_exception(self, scorecard):
    for i in range(20):
      scorecard.roll(5)
    with pytest.raises(ValueError):
      scorecard.roll(6)