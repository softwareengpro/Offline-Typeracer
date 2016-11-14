import socket, time,os, random

class Server():
  def __init__(self,Adress=('',5000),MaxClient=2):
      self.s = socket.socket()
      self.s.bind(Adress)
      self.s.listen(MaxClient)
  def WaitForConnection(self):
  	while 1:
  		self.Client, self.Adr=(self.s.accept())
  		print('Got a connection from: '+str(self.Client)+'.')
		self.Client.send('hello, how r u'.encode())
		a = self.Client.recv(1024).decode()
		print a

Stupid=Server()
Stupid.WaitForConnection()