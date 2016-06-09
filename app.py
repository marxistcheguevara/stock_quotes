from get_quotes import get_data_as_json
from bottle import request, Bottle, abort
app = Bottle()

@app.route('/')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')

    while True:
        try:
            message = get_data_as_json()
            wsock.send(message)
        except wse:
            break

from gevent.pywsgi import WSGIServer as ws
from geventwebsocket import WebSocketError as wse
from geventwebsocket.handler import WebSocketHandler as wsh
server = ws(("0.0.0.0", 8081), app, handler_class = wsh)
server.serve_forever()