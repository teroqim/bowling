from bottle import request, response, HTTPResponse, Response
import json
from bowlingapi.scorecard import Scorecard

def setup_endpoints(app):
  
  '''
  At this point, I'm thinking there will be just one endpoint in total. 
  It will accept the next roll and return an updated scorecard.
  
  Some initial thoughts:
  - Accept json-formatted data in body.
  - Accept an integer representing the number of pins knocked down.
  - First roll starts the game.
  - Always return an updated scorecard.
  - After the game ends, the next roll starts a new game.
  '''
  @app.route('/roll', method='POST')
  def roll():
    # Validate input

    # If no game or currenct game is finished, start new game

    # Roll

    # Return scorecard
    return json.dumps(request.json)

  return app