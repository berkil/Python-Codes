#!/usr/bin/python	

"""
| ~~~~~~~~~~~~~~~~~~~~~~~~ | ~~~~~~~~~~~~~~~~~~~ |
| Built By Boris Bakshiyev |       v1.0  	 |
| ~~~~~~~~~~~~~~~~~~~~~~~~ | ~~~~~~~~~~~~~~~~~~~ |
"""

import random																	                                      			   #importing the RANDOM library

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()[]_-? ' #defining the characters that the password will use
pwd = ''																					                                           #defining the variable that will contain the password
types = ['none','lower','upper','number','symbol']											                     #defining a list for character types for if statement to compare
last = types[0]																				                                       #variable for checking if two characters from the same type
x = 0																						                                             #counter for the while loop	

while (x < 10):																				                                       #while loop combining password of 10 unique characters
	
	next_index = random.randrange(len(alphabet))											                         #variablr for containing the current character to compare to the next character
	next_char = alphabet[next_index]														                               #variable for containing the next charecter to compare to the current charecter
	
	if next_char.islower():																	                                   #checking if the character is lower case
		next=types[1]																		
	elif next_char.isupper():																                                   #checking if the character is upper case
		next=types[2]
	elif next_char.isdigit():																                                   #cheking if the character is digit
		next=types[3]
	else:																					                                             #if the character isnt one of the above- its symbol
		next=types[4]

	if last != next:																		                                       #checking if the current character and the next charecter is the same case
		pwd = pwd + next_char																                                     #if not so the program continues, else the program chooses another character
		last=next 																			                                         #if the is statment is True, the next charecter will be added to the password
		x += 1 																				                                           #counter for charecter amount
	
print 'new password: ',pwd 																	                                 #printing the complete password
