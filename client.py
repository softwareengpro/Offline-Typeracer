import socket

class Client(adress):
   def __init__(self,Adress=('adress',5000)):
      self.s = socket.socket()
      self.s.connect(Adress)
      data = ''
      data = s.recv(1024).decode()
      print (data)
      self.s.send('fine'.encode())
