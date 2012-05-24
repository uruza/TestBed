#!/usr/bin/python
# Note, that WebsocketServer starts flash policy server by default
# so running this script is not strictly necessary

import sys
from websocket.policyserver import FlashPolicyServer
server = FlashPolicyServer(noisy=True)
server.start()
print >> sys.stderr, 'Listening on %s:%s' % (server.server_host, server.server_port)
server.serve_forever()
