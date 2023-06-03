# encoding : utf-8
# author : Ibrahim Lahlou
# code : client.py

import socket as skt

port=7999

print("",end="\n\n")
print("               TP1 Server")
print("_____________________________________________")

with skt.socket(skt.AF_INET,skt.SOCK_STREAM) as s:
	s.bind(('',port))
	s.listen()
	print('Listening ...')
	conn,addr = s.accept()
	with conn :
		print('Connected by :',addr)
		while True :
			data= conn.recv(1024)
			print("from client",repr(data.decode()))
			msg=input('server@vm1:7999$ ')
			conn.send(msg.encode())
			if msg == 'exit' :
				break
	s.close
