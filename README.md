# Bowling API
An API to keep score in a simple bowling game as described in instructions.md. (Except it is written in Python)

## Installation
- Install python 3 on your system
- Install pipenv (https://github.com/pypa/pipenv)
- Run ```pipenv install``` in repo root

## Running the server
```
pipenv run python3 scripts/run_server.py
```
Will start the API, listening on port 8080

## Playing the game
There's just one endpoint to use called 'roll'. You call it with the number of knocked-down pins in the next roll. You get an updated scorecard in return.

Using curl you can do this to roll:

```
curl localhost:8080/roll -XPOST -H "Content-Type: application/json" -d '{"pins_down":1}'
```

Further instructions:

- First roll starts the game.
- When game ends (i.e. after 10th frame is finished), the next roll starts a new game.

## Running tests
Run all tests:

```
pipenv run pytest
```
Run specific test:

```
pipenv run pytest -k "<class_name> and <method_name>"
```
