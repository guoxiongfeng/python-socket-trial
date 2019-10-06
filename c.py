import sys
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',9090))
while True:
    print('login, sign, or quit?')
    control_msg = input()
    if (control_msg == 'login' or control_msg == 'sign'):
        while True:
            print('Input two string for username and password seperate with whitespace:')
            u_p = input()
            if (len(u_p.split(' ')) != 2):
                print('Invalid input! Try again.')
            else: break
        send_msg = control_msg + ' ' + u_p
        client.send(send_msg.encode('utf-8'))
        recv_data = client.recv(1024)
        print('Response:',recv_data.decode())
    elif (control_msg == 'quit'):
        client.send('quit'.encode('utf-8'))
        data = client.recv(1024)
        print(data.decode())
        client.close()
        break
    else:
        print('Invalid Command. Try again.')