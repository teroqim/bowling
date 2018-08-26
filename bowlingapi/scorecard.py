
'''
Scorecard - Keep track of state in a game of bowling

Typical use case:

scorecard = new Scorecard()
scorecard.roll(3)
scorecard.roll(5)
...
scorecard.roll(5)

scorecard.to_dict()
-> {frames: <array>, score: <integer>}
'''
class Scorecard(object):
  def __init__(self):
    # Init 'internals'

    # Setup first frame
    pass

  def roll(self, pins_down):
    # If game is finished, do nothing

    # Validation of input

    # Figure out which frames to update:
    # - If last roll was a spare, add pins_down to that score
    # - If there was a strike within last 2 rolls, add pins_down to that score
    # - Add score to current frame
    pass

  def to_dict(self):
    # Create dict from internals with frames (including score breakdown for each) and total score
    # dict should be {frames: <array>, score: <integer>}
    pass
  
  def is_finished(self):
    # Check if we have reached 10 frames and finished the last one
    pass