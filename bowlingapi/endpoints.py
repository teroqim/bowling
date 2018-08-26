from bottle import request, response, HTTPResponse, Response
import json

def setup_endpoints(app):
  '''
  At this point, I'm thinking there will be just one endpoint in total. 
  It will accept the next roll and return an updated scorecard.
  
  Some initial thoughts:
  - Accept json-formatted data in body.
  - Accept an accept an integer representing the number of pins knocked down.
  - First roll starts the game.
  - The always return a scorecard.
  - After the game ends, the next roll starts a new game.
  '''
  @app.route('/roll', method='POST')
  def roll():
    return json.dumps(request.json)

  return app