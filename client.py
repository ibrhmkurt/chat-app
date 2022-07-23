import socket
import time

host_name = "localhost"
port = 7777

ethernet_socket = socket.socket()
ethernet_socket.connect((host_name,port))

print("baglanti saglandi!! {}:{}".format(host_name, port))

 
messeage = input("----::")
print("server bekleniyor..")

while messeage != "cikis":
	ethernet_socket.send(messeage.encode())
	data = ethernet_socket.recv(1024).decode()

	print ("SERVER : "+data)

	messeage = input("----::")
	print("server bekleniyor...")


ethernet_socket.close()