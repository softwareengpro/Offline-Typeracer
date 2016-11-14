import socket

class Client():
   def __init__(self,Adress=('10.100.106.83',5000)):
      self.s = socket.socket()
      self.s.connect(Adress)
      data = ''
      data = self.s.recv(1024).decode()	
      print data
      self.s.send('fne'.encode())

TC=Client()