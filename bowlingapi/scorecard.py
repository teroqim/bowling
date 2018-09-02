from functools import reduce

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
    self.score = None
    self.frames = []

  def _is_strike(self, frame):
    # Assumes first value is always a valid integer
    return (frame is not None) and frame['first'] >= 10

  def _is_spare(self, frame):
    # Assumes:
    # - First value is always a valid integer 
    # - A strike is not a spare
    if frame is None:
      return False

    return (not self._is_strike(frame)) \
      and frame['second'] is not None \
      and (frame['first'] + frame['second'] == 10)

  def _create_frame(self, first=None, second=None):
    return {
      'first': first,
      'second': second
    }

  def _is_closed(self, frame):
    return self._is_strike(frame) or frame['second'] is not None

  def _set_value_in_frame(self, frame, value):
    if frame['first'] is None:
      frame['first'] = value
    else:
      frame['second'] = value

  def _recalc_score(self, frames):
    def frame_score(frame):
      if frame['second'] is None:
        return frame['first']
      return frame['first'] + frame['second']

    return reduce(lambda agg, cur_frame: agg + frame_score(cur_frame), frames, 0)

  def roll(self, pins_down):
    # If game is finished, rase exception
    if self.is_finished():
      raise ValueError('Game finished')

    # Validation of input
    if pins_down < 0 or pins_down > 10:
      raise ValueError('Outside bounds')

    # If first roll, init game
    if len(self.frames) == 0:
      self.frames.append(self._create_frame(pins_down))
      self.score = pins_down
      return

    last_frame = self.frames[-1]

    # If this is the second roll in a frame, check if frame sum is within bounds
    if not self._is_strike(last_frame) \
      and last_frame['second'] is None \
      and last_frame['first'] + pins_down > 10:
      raise ValueError('Frame sum invalid')

    # If strike or spare in previous roll(s), update accordingly
    # We assume if the last frame was strike, there is no spare
    second_to_last_frame = self.frames[-2] if len(self.frames)>1 else None
    create_new_frame = False
    if self._is_strike(last_frame):
      # Note that if there was a strike in the last frame, 
      # then the current roll must be the first roll after the strike 
      # and we should (later) a create new frame.
      # If there also was a strike in the frame before the last, 
      # then it is the second roll after that strike and we should update that frame too.
      last_frame['first'] += pins_down
      create_new_frame = True
      if second_to_last_frame is not None and self._is_strike(second_to_last_frame):
        second_to_last_frame['first'] += pins_down
    elif second_to_last_frame is not None and self._is_strike(second_to_last_frame) and last_frame['second'] is None:
      # Just to be explicit, this means the second to last frame was a strike and thus
      # had no second roll.
      # Since the last frame did not have a strike and is not finished the current roll
      # must be the second roll in the frame.
      # We need to update the value for the strike, but not create a new frame
      second_to_last_frame['first'] += pins_down
    
    if self._is_spare(last_frame):
      # Since we assume a spare is distinct from a strike
      # This can only happen if the last frame was not a strike
      # and the current roll is the first roll after the spare.
      last_frame['second'] += pins_down
      create_new_frame = True
    elif last_frame['second'] is not None:
      # So last frame is neither strike nor spare
      # If there is no second value, it must mean we 
      # 'filled up' the last frame and need to create a new one
      create_new_frame = True
    
    if create_new_frame:
      self.frames.append(self._create_frame(pins_down))
    else:
      # No new frame means we must have a second roll in a frame
      last_frame['second'] = pins_down

    self.score = self._recalc_score(self.frames)

  def to_dict(self):
    # Create dict from internals with frames (including score breakdown for each) and total score
    # dict should be {frames: <array of frames>, score: <integer|None>}
    # A frame has the format {first: <integer>, second: <integer|None>}
    return {
      'score': self.score,
      'frames': self.frames
    }
  
  def is_finished(self):
    # Rule out any incorrect frame length
    return len(self.frames) >= 10 and self._is_closed(self.frames[-1])