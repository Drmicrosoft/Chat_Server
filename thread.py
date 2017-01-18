#!/usr/bin/python

import thread
import time

# Define a function for the thread
def print_time( threadName, delay):
	if delay == 4 :
	   while 1:
		  time.sleep(1)
		  print "omar"
	elif delay == 2 : 
		
	   while 1:
		  x = raw_input("")
		  print x

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass
