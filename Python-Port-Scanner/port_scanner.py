#!/usr/bin/python

"""
| ~~~~~~~~~~~~~~~~~~~~~~~~ | ~~~~~~~~~~~~~~~~~~~ |
| Built By Boris Bakshiyev |       v1.0  	 |
| ~~~~~~~~~~~~~~~~~~~~~~~~ | ~~~~~~~~~~~~~~~~~~~ |
"""

import socket,os																					#importing the socket library and the os library
from sys import argv																				#importing the argv function from the sys library

socket.setdefaulttimeout(2)																			#setting the time out - because the default is to long-  10 seconds!!
	
def BannerGrabber(ip,port):																			#function for grabbing the banner
	opening = socket.socket()																		#defining the socket
	msg = []																						#declering the msg list variable

	try:
		opening.connect((ip,port))																	#opening connection to specific ip and port number
		banner = str(opening.recv(1024))															#defining to grab the first 1024 bytes- acceptet to be banner message
		print '[+]',ip+':'+str(port),' Service:',banner												#printing the banner
		if banner in msg:																			#before we save the banner- we need to check if its already exist.
			pass																					#is yes- so we wont save it, if not we will save it.
		else:
			msg.append(banner)			    	  													#adding the banner message to list
			banner_log = open ('banner.txt','a+')													#opening the banner file in append format
			banner_log.write('\t\t IP: '+str(ip)+'\t'+'Port: '+str(port)+'\t\t'+banner+'\n')		#writing the unique banner into the file
	except Exception , e:
		print '[+] Error: ip='+ip+':'+str(port), 'message:',str(e)									#printing the error if the port is closed

def main():																							#the main function that composes the IP address and the port number
	try:
		targets_file = open(argv[1],'r')															#opening the targets IP file
		targets = targets_file.read().split()														#inserting all the targets IP into array

		ports_file = open(argv[2],'r')																#opening the targets port number file
		ports = ports_file.read().split()															#inserting all the targets port number into array

		for i in range (len(targets)):																#starting for loop that depends on the IP
			for j in range (len(ports)):															#starting for loop that combines IP address to range of port numbers
				BannerGrabber(targets[i],int(ports[j]))												#calling the banner grabing function
	except:
		print 'You have to write the targets file and the ports file!!'								#printing message if the IP file or port file is missing

os.system('clear')																					#clearing the screen before printing the result
main()																								#calling the main function to start combining IP addresses and port numbers
