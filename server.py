# server side program

import socket 
import sys
import os
import threading
import time
num_of_thread=2
threadlst=[1,2]
connection_obj=[]
connection_addr=[]

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
        s.bind(('',port))
        s.listen(5)
    except socket.error as tag:
        print str(tag)
        bind_socket()

def accept_connection():
    for i in connection_obj:
        i.close()
    del connection_obj[:]
    del connection_addr[:]
    while 1:
        try:
            c,addr=s.accept()
            c.setblocking(1)
            connection_obj.append(c)
            connection_obj.append(addr)
        except:
            print "error accepting connection"
            




        
def main():
    create_socket()
    bind_socket()
   

main()        
           
