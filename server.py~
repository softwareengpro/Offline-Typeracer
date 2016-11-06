# server side program

import socket 
import sys
import os
import threading
import time
from queue import Queue

num_of_thread=4
threadlst=[1,2,3,4]
queue=Queue()
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
        s.bind((host,port))
        s.listen(5)
    except socket.error as tag:
        print str(tag)
        bind_socket()

def accept_socket():
    c, addr=s.accept()
    print "connected client is",addr 
    send_msg(c)
    c.close()

def send_msg(c):
    while(True):
        print " send a msg to client"
        m=raw_input()
    if(m=='quit'):
        c.close()
        s.close()
        sys.exit()
    if(len(m)>0):
        c.send(m)
        client_responce=c.recv(1024)
        print client_responce
        
def main():
    create_socket()
    bind_socket()
    accept_socket()

main()        
           
