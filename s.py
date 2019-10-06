import Server
import sys
import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',9090))
server.setblocking(True)
server.listen(5)
while True:
    conn,addr = server.accept()
    print(conn,addr)
    while True:
        data = conn.recv(1024)
        tmp = data.decode()
        if (len(data) > 0):
            print('Receive:',tmp)
            if (tmp == 'quit'): 
                conn.send('Connection Ended'.encode('utf-8'))
                break
            state = Server.dealing_msg(tmp)
            conn.send(state.encode('utf-8'))