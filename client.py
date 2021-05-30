import hashlib 
from base64 import b64encode, b64decode
import socket

ip= (input('Direccion IP a conectar: '))
u= (input('Nombre de usuario: '))
flag = 1

try:

	if (flag==1):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, 19876))
		cod = ("helloiam "+u).encode("UTF-8")
		s.send(cod)
		data = s.recv(1024)
		flag=2

	if(flag==2):
		cod = ("msglen").encode("UTF-8")
		s.send(cod)
		data = s.recv(1024)
		flag=3

	if(flag==3):
		u = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		u.bind(("",9876))
		u.settimeout(15)
		cod = ("givememsg 9876").encode("UTF-8")
		s.send(cod)
		data = s.recv(1024)
		data2,addr = u.recvfrom(4096)
		print("Su mensaje es: ")
		print(b64decode(data2).decode("UTF-8"))
		chk = hashlib.md5(b64decode(data2)).hexdigest()
		cod = ("chkmsg "+chk).encode("UTF-8")
		s.send(bytes("chkmsg "+chk,"UTF-8"))
		data = s.recv(1024)
		flag=4

	if(flag==4):
		cod = ("bye").encode("UTF-8")
		s.send(bytes(cod))
		data = s.recv(1024)


except socket.timeout as e:  
	print ("Ocurrio un error por tiempo espera superado del UDP")

except Exception as e:  
	print (e)
