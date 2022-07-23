import socket
import time

host_name = "localhost"
port = 7777

ethernet_socket = socket.socket()
ethernet_socket.bind((host_name,port))
ethernet_socket.listen(1)

connection, address = ethernet_socket.accept()

print(str(address)+" baglanti saglandi.")

while True:
	while True:
		try:
			data = str(connection.recv(1024).decode())
			print("client sunu yolladi : "+ data)
			break
		except ConnectionResetError:
			time.sleep(2)
			connection, address = ethernet_socket.accept()
			print(str(address)+ " baglanti saglandi.")

	if data == "cikis":
		break
	else:
		messeage = input("----::")
		print("client bekleniyor...")
		connection.send(messeage.encode())

connection.close()
