import os
import socket                  

class Server():

    def sendFile(self):
        port = 60001  
        s = socket.socket() 
        host = socket.gethostname() 
        s.bind((host, port)) 
        s.listen(1)  
        print('Server is ready!!')
        while True:
            (conn, addr) = s.accept()     
            print('Got connection from', addr)
            try:
                pathName = os.getcwd()
                dir = open('dir_info.txt', 'w')
                for x in os.listdir(pathName):
                    if os.path.isfile(x):
                        dir.write('f-' + ' ' + x)
                    elif os.path.isdir(x):
                        dir.write('d-' + ' ' + x)
                    elif os.path.islink(x):
                        dir.write('l-' + ' ' + x)
                    else:
                        dir.write(' ' + ' ' + x)
                    dir.write('\n')
                dir.close()

            except NotADirectoryError:
                print('Oops directory not found')
            print('Sending server directory information......')
            f = open('dir_info.txt', 'r')
            l = f.read(1024)
            while l:
                conn.send(l.encode())
                l = f.read(1024)
            f.close()
            conn.close()
            print('Server directory information sent!!')

            port = 60002  
            s = socket.socket()  
            host = socket.gethostname()  
            s.bind((host, port))  
            s.listen(1)  

            print('Sending file....')
            while True:
                (conn, addr) = s.accept()     
                file = conn.recv(1024)
                filename = file.decode('utf-8')
                if os.path.isfile(filename):
                    conn.send(str.encode("EXISTS " + str(os.path.getsize(filename))))
                    f = open(filename, 'rb')
                    l = f.read(1024)
                    while l:
                        conn.send(l)
                        l = f.read(1024)
                    f.close()
                    print('Done sending!')
                    conn.close()
                    print('Connection Closed!')

                else:
                    print('File not found')
                    conn.close()
                    print('Connection Closed!')


serverOne = Server()
serverOne.sendFile()
