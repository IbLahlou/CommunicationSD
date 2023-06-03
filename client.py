# encoding : utf-8
# author : Ibrahim Lahlou
# code : client.py

import socket as skt

host='192.168.100.4'
port=7999

print("",end="\n\n")
print("                TP1 CLI")
print("_____________________________________________")

with skt.socket() as s:
	s.connect((host,port))
	while True :
		msg=input('client@vm2:7999$ ')
		s.sendall(msg.encode())
		data = s.recv(1024).decode()
		print("from server",data)
		if msg == 'exit' :
			break
	s.close
