import os
import socket
class Client():

    def receiveFile(self):
        s = socket.socket()  
        host = socket.gethostname() 
        port = 60002 
        s.connect((host, port))
        recfile = input()
        s.send(str.encode(recfile))
        data = s.recv(1024).decode('utf-8')
        if data[:6] == 'EXISTS':
            filesize = data[6:]
            with open('new_' + recfile, 'wb') as f:
                print('file opened')
                totalRecv = 0
                while True:
                    print('receiving data...')
                    data = s.recv(1024)
                    totalRecv += len(data)
             
                    print("{0:.2f}".format((totalRecv / float(filesize)) * 100) + "% Done")
                    if not data:
                        break
                    f.write(data)

            f.close()
            print('Successfully get the file')
            s.close()
        else:
            print('File not found')
            s.close()
            print('Connection Closed!')



    def receiveDirInfo(self):
        s = socket.socket()
        host = socket.gethostname() 
        port = 60001  
        s.connect((host, port))
        print('Receiving directory information....')
        with open('dir_info.txt', 'w') as f:
            while True:
                list = s.recv(1024).decode()
                if not list:
                    break
                f.write(list)

        f.close()
        dir_info = open('dir_info.txt', 'r')
        print(dir_info.read())
        s.close()

        s = socket.socket() 
        host = socket.gethostname()  
        port = 60002  
        s.connect((host, port))
        recfile = input()
        s.send(str.encode(recfile))
        data = s.recv(1024).decode('utf-8')
        if data[:6] == 'EXISTS':
            filesize = data[6:]
            with open('new_' + recfile, 'wb') as f:
                print('file opened')
                totalRecv = 0
                while True:
                    print('receiving data...')
                    data = s.recv(1024)
                    totalRecv += len(data)
                    print("{0:.2f}".format((totalRecv / float(filesize)) * 100) + "% Done")
                    if not data:
                        break
                    f.write(data)

            f.close()
            print('Successfully get the file')
            s.close()
        else:
            print('File not found')
            s.close()
            print('Connection Closed!')

clientOne = Client()
iteration = 0
while True:
    print('Press "1" to receive a file from server or press "2" exit....')
    choice = int(input())
    if choice == 1 and iteration == 0:
        clientOne.receiveDirInfo()
        iteration = iteration + 1
    elif choice == 1 and iteration != 0:
        clientOne.receiveFile()
    elif choice == 2:
        break
