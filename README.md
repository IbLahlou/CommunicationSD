# Compte rendu TP1 Mode Connecté


## 0. Programmation de Socket

Création d'un programme communicant des sockets avec python entre les deux machine VM1 et VM2 des instances d'ubuntu server



.
### 1 . Architecture réseau de cette manipulation

- **Réseau NAT**
![Nat network](Pasted image 20230323083318.png)

#### Les modèles d'architecture de communication

![[Pasted image 20230325101611.png]]

Dans ce tp on utilisera l'interface réseau ethernet "eth0" pour communication entre sockets .

### 2. Architecture Client-Server 

Dans le module socket de python 
![[Pasted image 20230325103734.png]]

1) Etablissement de connection (3-vay handshake)liason à trois voies
2) Transfére de donnée entre client et server
3) Fermeture de la communication entre client et server

Au mode Connecté , on spécifie un socket de flux. pour une communication fiable



### 3. Programmation

Le module socket de Python fournit une interface à l’API des sockets de Berkeley.

Python fournit une API pratique et cohérente qui mappe directement aux appels système, leurs homologues C.

Voir la docummentation de python-socket  :
[Programmation de sockets en Python (Guide) - Real Python](https://realpython.com/python-sockets/)


#### 3.1. Programmation coté client
![[Pasted image 20230325111836.png]]
```python
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
```

#### 3.2 Programmation coté serveur
![[Pasted image 20230325113437.png]]
```python
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
```



SOCK_STREAM : Spécifie un socket de flux. Doit être fourni lorsqu’un client ou un serveur basé sur une connexion de streaming est nécessaire et sera utilisé pour une communication fiable , utilisant le protocole TCP
### 5. Éxecution du Programme

0. Verification du port
```bash 
netstat -an
sudo lsof -i :7999
```

![[Pasted image 20230325115047.png]]
![[Pasted image 20230325115051.png]]
Le port n'est pas occupé , on peut donc l'utilisez pour la communication client-server

sinon on pourra utilisez la commande kill

```bash
sudo kill 12345
```

1. Éxecution du server 
Server :
![[Pasted image 20230325115205.png]]
le server attends le client pour qu'il se connecte ...

2. Éxecution du client
Client :
![[Pasted image 20230325120427.png]]
le client se connecte au server
Server : 
![[Pasted image 20230325120452.png]]
le server accepte la connection du client 

3. Transfére de donné depuis le client
Client :
![[Pasted image 20230325120815.png]]
Envoie de donné , le client attends le retour du server

Server :
![[Pasted image 20230325120846.png]]
Réception de donné , le server peut répondre

4. Transfére de donné depuis le server

Server :
![[Pasted image 20230325121008.png]]
Envoie de donné , le server attends le retour du server

Client :
![[Pasted image 20230325121121.png]]
Réception de donné , le client peut répondre

5. Fermeture de la session

Client : 
![[Pasted image 20230325121226.png]]
Le client mets fin à la communication
