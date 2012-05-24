import traceback
from json import dumps


class Application(object):

    def __init__(self):
        self.buffer = []
        self.users = set()

    def __call__(self, environ, start_response):
        socket = environ.get('websocket')
        if socket is not None:
            self.handle_websocket(socket)
        else:
            path = environ['PATH_INFO'].strip('/')
            if not path:
                start_response('200 OK', [('Content-Type', 'text/html')])
                return ['<h1>Welcome. Try the <a href="/chat.html">chat</a> example.</h1>']

            if path in ['json.js', 'chat.html']:
                try:
                    data = open(path).read().replace('$PORT', str(PORT))
                except Exception:
                    traceback.print_exc()
                    return not_found(start_response)
                start_response('200 OK', [('Content-Type', 'text/javascript' if path.endswith('.js') else 'text/html'),
                                          ('Content-Length', str(len(data)))])
                return [data]
        return not_found(start_response)

    def handle_websocket(self, socket):
        socket.send(dumps({'buffer': self.buffer}))
        socket.sessionid = '%s:%s' % socket.getpeername()
        announcement = '%s connected' % socket.sessionid
        self.broadcast(dumps({'announcement': announcement}), socket.sessionid)
        self.users.add(socket)
        try:
            while True:
                message = socket.receive()
                if message is None:
                    announcement = '%s disconnected' % socket.sessionid
                    self.broadcast(dumps({'announcement': announcement}), socket.sessionid)
                    break
                else:
                    message = {'message': [socket.sessionid, message]}
                    self.buffer.append(message)
                    if len(self.buffer) > 15:
                        del self.buffer[0]
                    self.broadcast(dumps(message), socket.sessionid)
        finally:
            self.users.discard(socket)

    def broadcast(self, message, me=None):
        print message
        for socket in self.users:
            if socket.sessionid != me:
                try:
                    socket.send(message)
                except IOError:
                    self.users.discard(message)


def not_found(start_response):
    start_response('404 Not Found', [])
    return ['<h1>Not Found</h1>']


if __name__ == '__main__':
    from websocket.server import WebsocketServer
    PORT = 8000
    WebsocketServer(('', PORT), Application()).serve_forever()
