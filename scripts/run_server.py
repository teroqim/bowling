from bottle import Bottle
from bowlingapi.endpoints import setup_endpoints

if __name__ == '__main__':
  app = Bottle()
  setup_endpoints(app)
  app.run(port=8080, host='0.0.0.0', reloader=True)