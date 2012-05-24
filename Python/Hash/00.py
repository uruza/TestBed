# WebSocket Version 13(뒤에것)

import hashlib
import base64

m = hashlib.sha1()
m.update(b"dGhlIHNhbXBsZSBub25jZQ==258EAFA5-E914-47DA-95CA-C5AB0DC85B11")
encoded = base64.b64encode( m.digest() )
print( encoded )
