import socket

HOST = '192.168.9.100'    # The remote host
PORT = 8123              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1 :
		

	print s.recv(1000)
	x = raw_input(" your message : ")
	s.sendall(x)
s.close()
print "omar"
