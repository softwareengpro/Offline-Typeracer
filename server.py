# server side program

import socket 
import sys

def create_socket():
    try:
        global host
        global port
        global s
        host=""
        port=12345
        s=socket.socket()
    except socket.error as tag:
        print str(tag)

def bind_socket():
    try:
        global host
        global port
        global s
        s.bind((host,port))
        s.listen(5)
    except socket.error as tag:
        print str(tag)
        bind_socket()

def accept_socket():
    c, addr=s.accept()
    print "connected client is"+"IP" +addr[0] + "port" +addr[1]
    send_msg(c)
    c.close()

def send_msg(c):
    while(true):
        m=raw_input()
        if(m=='quit'):
            c.close()
            s.close()
            sys.exit()
        if(len(str.encode(m)>0)):
            c.send(str.encode(m))
            client_responce=str(c.recv(1024),"utf-8")
            print client_responce
        
def main():
    create_socket()
    bind_socket()
    accept_socket()

main()        
           
