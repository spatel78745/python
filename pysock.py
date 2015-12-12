import _thread as thread, time
from socket import *

myHost = ''
myPort = 50006
serverHost = ''
serverPort = 50006
testChunk = b'this is a line\nand another line\nand line 3\nand some leftover'

"""
Chunk consists may consist of full lines and a remaining chunk
- Full lines end in '\n'
- The remaining chunk doesn't end in '\n'

Example:
    this is a full line\nand another full line\n, and the remaining chunk
    
This function an iterator over the non-empty (i.e. not equal to '\n'), full lines
and the remaining chunk
"""
def partitionChunk(chunk):
    lines = chunk.splitlines(True)
    print('lines: ', lines)
    
    # Filter out full lines
    cmdsWithEnds = filter(lambda x: x[-1] == '\n', lines)

    # Strip the '\n'
    cmdsWithEmpties = (cmd.rstrip() for cmd in cmdsWithEnds)

    # And now filter out any empty lines
    cmds = (cmd for cmd in cmdsWithEmpties if cmd != '\n')

    # What's left over is a partial command...the rest is still in the socket
    chunk = chunk.rpartition('\n')[-1]

    return cmds, chunk

"""
Processes commands on a socket
"""
def server(responder):
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.bind((myHost, myPort))
    sockobj.listen(1)
    
    print('Waiting for connection.');
    connection, address = sockobj.accept()
    print('Connected.');

    chunk = ''
    try:
        while True:
            chunk += connection.recv(80)
            if not chunk:
                print('Connection closed.')
                raise OSError;

            commands, chunk = partitionChunk(chunk)

            for cmd in commands:
                if not connection.sendall(responder(cmd)) is None:
                    print('sendall failed')
                    raise OSError        
    finally:        
        connection.close()
        sockobj.close()
        
def echoResponder(msg):
    print('Received: ', msg)
    return b'Echo=>' + msg + b'\n' 

def client(*args):
    messages = (x.encode() for x in args)
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.connect((serverHost, serverPort))
    
    for line in messages:
        sockobj.send(line)
        data = sockobj.recv(1024)
        print('Client received: ', data)
        
    sockobj.close()

def testPartitionChunk():
    def tr(s):
        if   s == '\n': return 'endl'
        elif s == ''  : return "''"
        else          : return s
        
    def printCommands(commands):
        print('===== commands =====')
        for cmd in commands:
            print('\t', tr(cmd))
        print('===== end commands =====')
        

    def doCase(case):
        print('begin case: ', tr(case))
        commands, chunk = partitionChunk(case)
        print('chunk: ', tr(chunk))
        printCommands(commands)
        print('end case: ', tr(case), '\n\n')

    doCase('')
    doCase('\n')
    doCase('no lines')
    doCase('a line\nand a chunk')
    doCase('a line\nand no chunk\n')

if __name__ == '__main__':
    testPartitionChunk()
