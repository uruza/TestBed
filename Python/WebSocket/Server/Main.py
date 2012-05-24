
import socket

import hashlib
import base64


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 9999))
sock.listen(5)

handshake = '\
HTTP/1.1 101 Switching Protocols\r\n\
Upgrade: websocket\r\n\
Connection: Upgrade\r\n\
Sec-WebSocket-Accept: \
'
handshaken = False

print("TCPServer Waiting for client on port 9999")

import sys

data = ''
header = ''

client, address = sock.accept()

print( '============== Start ==============')

header = client.recv(256).decode()
#print( header )
#print( '============================')

key = header.split('\r\n')[5]
key = key.split( ': ' )[1]
key = key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
#print( key )
#print( '============================')

m = hashlib.sha1()
m.update(key.encode())
encoded = base64.b64encode( m.digest() )
key = encoded.decode()
#print( key )
#print( '============================')

handshake += key + '\r\n\r\n'
#print ( handshake )
#print( '============================')

client.send( handshake.encode() )

recv = client.recv(512)#.decode()
print ( recv )
#print( '============================')
recv = client.recv(512)#.decode()
print ( recv )
#print( '============================')
recv = client.recv(512)#.decode()
print ( recv )
#print( '============================')
recv = client.recv(512)#.decode()
print ( recv )
#print( '============================')
recv = client.recv(512)#.decode()
print ( recv )
#print( '============================')

"""
while True:
    if handshaken == False:
        header += client.recv(256).decode()

        if header.find('\r\n\r\n') != -1:
            print( header )
            key = header.split('\r\n')[5]
            key = key.split( ': ' )[1]
            key = key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
            print( key )
            
            m = hashlib.sha1()
            m.update(key.encode())
            encoded = base64.b64encode( m.digest() )
            key = encoded.decode()
            print( key )
            print( '============================')

            handshake += key + '\r\n'
            print ( handshake )

            client.send( handshake.encode() )
            
            
            m = hashlib.sha1()
            m.update(b"dGhlIHNhbXBsZSBub25jZQ==258EAFA5-E914-47DA-95CA-C5AB0DC85B11")
            encoded = base64.b64encode( m.digest() )
            print( encoded )
            

            
            data = header.split('\r\n\r\n', 1)[1]            
            handshaken = True
            client.send( handshake.encode() )
            print( handshake )
            
    else:
        tmp = client.recv(128).decode()        
        data += tmp;
        validated = []

        msgs = data.split('\xff')
        data = msgs.pop()

        for msg in msgs:
            if msg[0] == '\x00':
                validated.append(msg[1:])

        for v in validated:
            print ( v )
            client.send('\x00' + v + '\xff')
"""
