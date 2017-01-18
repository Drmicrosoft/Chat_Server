#!/usr/bin/python

import thread
import time

import getpass
import sys
import telnetlib

HOST = "192.168.9.100"
port = 8123
tn = telnetlib.Telnet(HOST,port)

print tn.read_until("What's your name?")

# Define a function for the thread
def print_time( threadName, delay):
	i = 1 
	if delay == 2 :
	   while 1:
		  y = tn.read_eager()
		  if(y != ""):
						print y 
						y=""
						
				
	elif delay == 4 : 
		
	   while 1:
				if(i == 1 ):
					x = raw_input ("")
					i=2
				else :
					if(x != ""):
						tn.write(x+"\r\n")
						x=""
						i=1
				

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass

