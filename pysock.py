from socket import *

myHost = ''
myPort = 50006
serverHost = ''
serverPort = 50006

def echoServer():
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.bind((myHost, myPort))
    sockobj.listen(5)

    connection, address = sockobj.accept()
    
    while True:
        data = connection.recv(1024).rstrip()
        if (not data) or (data == b'stop'): break
        connection.send(b'Echo=>' + data + '\n')
        
    connection.close()

def client(*args):
    messages = (x.encode() for x in args)
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.connect((serverHost, serverPort))
    
    for line in messages:
        sockobj.send(line)
        data = sockobj.recv(1024)
        print('Client received: ', data)
        
    sockobj.close()

if __name__ == '__main__':
    client('all composite phenomena are impermanent\n',
           'all contaminated things and events are unsatisfactory\n')
