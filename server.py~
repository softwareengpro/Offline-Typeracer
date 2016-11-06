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


        
def main():
    create_socket()
    bind_socket()
   

main()        
           
