from socket import *

myHost = ''
myPort = 50006
serverHost = ''
serverPort = 50006

def server(responder):
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.bind((myHost, myPort))
    sockobj.listen(5)
    
    print('Waiting for connection.');
    connection, address = sockobj.accept()
    print('Connected.');
    
    while True:
        data = connection.recv(1024).rstrip()
        if (not data):
            print("Connection closed.")
            break
        
        connection.send(responder(data.decode()).encode())
        
    connection.close()
    sockobj.close()
        
def echoResponder(message):
    return 'Echo=>' + message + '\n' 

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
#    client('all composite phenomena are impermanent\n',
#           'all contaminated things and events are unsatisfactory\n')
    server(echoResponder)
