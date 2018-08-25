# Bowling Code Challenge

* Please create a repository in GitHub (or a similar service) so that we can follow your progress.
* The implementation should use either Javascript, Go.
* Remember that we are more interested how you approach this problem than seeing you complete all the features (if you don't have enough time to finish everything, simply explain how you would continue the implementation).

## Minimum requirements

* Implement a scoring system for a bowling game according to these rules:
  - A game consists of 10 frames.
  - In general each frame has 2 rolls.
  - In general a player scores the number of pins knocked down.
  - If the player knocks down all 10 pins on the first roll, it’s a strike. The player scores 10 plus the number of pins knocked down in the next two rolls.
  - If the player needs two rolls to knock down all 10 pins, it’s a spare. The player scores 10 plus the number of pins knocked down in the next roll.

## Optional requirements

* Add support for the last frame in the game:
  - The player gets additional rolls in the last frame: one additional roll for a spare or two additional rolls for a strike.

* a frontend to your API so you can roll one ball at a time
* Or any other fun feature you can think of. :)

## What we want to see

* a git repository with history would be ideal, but any documentation about your steps is great.
* unit tests + acceptance test (TDD or BDD preferred but not required)