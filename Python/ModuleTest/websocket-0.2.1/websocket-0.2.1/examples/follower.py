import traceback
from time import time
from datetime import datetime
import gevent
from gevent.pool import Pool


class Application(object):

    def __init__(self):
        self.sockets = set()
        self.pool = Pool(1024)

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO'].strip('/')
        socket = environ.get('websocket')
        if socket is not None:
            gevent.spawn(self.receive, socket)
            self.sockets.add(socket)
        else:
            return self.serve_file(path, start_response)

    def serve_file(self, path, start_response):
        if path != 'json.js':
            path = 'follower.html'
        try:
            data = open(path).read().replace('$PORT', str(PORT))
        except Exception:
            traceback.print_exc()
            start_response('404 Not Found', [])
            return ['<h1>Not Found</h1>']
        start_response('200 OK', [('Content-Type', 'text/javascript' if path.endswith('.js') else 'text/html'),
                                  ('Content-Length', str(len(data)))])
        return [data]

    def send(self, socket, message):
        try:
            socket.send(message)
        except:
            self.sockets.discard(socket)
            raise

    def receive(self, socket):
        try:
            peer = socket.getpeername()
            message = socket.receive()
            assert message is None, repr(message)
            print '%s:%s Remote side closed the websocket connection.' % peer
        except IOError, ex:
            print '%s:%s %s' % (peer[0], peer[1], ex)
        finally:
            self.sockets.discard(socket)

    def update(self):
        while True:
            now = datetime.now()
            message = '%s (%s client%s)' % (now, len(self.sockets), 's' if len(self.sockets) != 1 else '')
            start = time()
            for socket in list(self.sockets):
                self.pool.spawn(self.send, socket, message)
            sleep = 0.1 - (time() - start)
            if sleep > 0:
                gevent.sleep(sleep)
            else:
                print 'Skipped sleeping'


if __name__ == '__main__':
    from websocket.server import WebsocketServer
    PORT = 8000
    app = Application()
    updater = gevent.spawn_link(app.update)
    server = WebsocketServer(('', PORT), app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    app.pool.join()
