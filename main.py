import socket
import threading

host = '192.168.56.1'
port=5252
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nickname = input('Enter your nickname: ')
client.connect((host,port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Error occured")
            client.close()
            break



def write():
    while True:
            message = '{}: {}'.format(nickname, input(''))
            client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
