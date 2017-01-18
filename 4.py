
import getpass
import sys
import telnetlib

HOST = "192.168.9.100"
port = 8123
tn = telnetlib.Telnet(HOST,port)

print tn.read_until("What's your name?")

while 1 :
	y = tn.read_eager()
	print y
	x = raw_input ("your message :")
	tn.write(x+"\r\n") 
		
	
	
	
	
	

print tn.read_all()
