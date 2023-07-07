# encoding : utf-8
# author : Ibrahim Lahlou
# Code : client_rpc.py

import rpyc

conn = rpyc.connect("192.168.100.4",7000)

print("                                          TP3 RPC client")
print("---------------------------------------------------------------------------------------")
print("We'll calculate the sum of a & b ...")

while True :
    a = int(input("a = "))
    b = int(input("b = "))
    result =conn.root.add(a,b)
    print("a+b = ",result)
    print("")
    c=input("exit (y/n) :")
    if c=='y':
        break
    print("")
    
