#!/user/bin/python

"""
| ~~~~~~~~~~~~~~~~~~~~~~~~ | ~~~~~~~~~~~~~~~~~~~ |
| Built By Boris Bakshiyev |       v1.0  	 |
| ~~~~~~~~~~~~~~~~~~~~~~~~ | ~~~~~~~~~~~~~~~~~~~ |
"""

import time, os, sys

count=8															                    #variablefor loop counting
os.system('clear')												              #clear the screen before program starts

while count != 4:												                #loop for printing '>'								
	print '>',
	sys.stdout.flush()
	time.sleep(.2)
	count -= 1

time.sleep(.2) 													                #delay of 0.2 seconds
print 'Password ', 
sys.stdout.flush()												              #clearing the buffer
time.sleep(.4)													                #delay of 0.4 seconds
print 'Complexity ',
sys.stdout.flush()												              #clearing the buffer
time.sleep(.4)													                #delay of 0.4 seconds
print 'Checker ',				
sys.stdout.flush()												              #clearing the buffer
time.sleep(.2)													                #delay of 0.2 seconds

		
while count != 0:												                #loop for printing '<'
	print '<',
	sys.stdout.flush()
	time.sleep(.2)
	count -= 1

print '\n  The Password Has To Be Assembled Of: '	
time.sleep(2)													                    #delay of 2 seconds
print '1. At least 8 characters.'						
time.sleep(1)													                    #delay of 1 second
print '2. At least one uppercase letter.'
time.sleep(1)													                    #delay of 1 second
print '3. At least one lowercase letter.'
time.sleep(1)													                    #delay of 1 second
print '4. At least one symbol. \n'
time.sleep(2)													                    #delay of 2 seconds


checker = 0														                    #defining variable needed for the while loop- of the password checker
sym = '!'														                      #defining variable of symbole case


while checker < 5 :												                #while loop that checks if the password is good to go

	checker = 0												                    	#defining  variable needed for the while loop- of the password checker
	os.system ('clear')											                #clearing the screen
	sys.stdout.flush()											                #clearing the buffer
	print '> > > > Password Complaxity Checker < < < <'		
	password = raw_input('Pleas Enter Your Password: ')			#asking from the user to enter his password, and saving it in variable named password
	print '\t The password being analyzed.... '				
	
	time.sleep(0.2)												                  #delay of 0.2 seconds

	if len(password) < 8 :										              #if statement that checking if the length of the password is at least 8 characters
		print '\tYou do not have at least 8 charecters'			  #if the password less then 8 charecters this massage will be printed
		time.sleep(0.5)											                  #delay of 0.5 seconds
	else:													
		checker += 1											                    #if the password has at least 8 characters the counter "checker" will count that one of 5 statments is true
	
	if any(p.islower() for p in password) :						      #checking if the password contains at least one lowercase letter
		checker +=1												                    #if the password has at least 1 lowercase letter the counter will count it
	else:
		print '\tYou do not have at least one lowercase letter'
		time.sleep(1)											                    #delay of 1 second

	if any(p.isupper() for p in password):						      #checking if the password has at least one uppercase letter
		checker += 1											                    #if the password has at least 1 uppercase letter the counter will count it
	else:
		print '\tYou dont have at least on uppercase letter'
	time.sleep(1)												                    #delay of 1 second
	
	if any(p.isdigit() for p in password):						      #checking if the password contains at least 1 digit
		checker +=1												                    #if the password contains at least 1 digit the counter will count is
	else:
		print '\tYou dont have at least on number'

	if password.isalnum() == sym.isalnum():						      #checking if the password contains at least one symbol.
		checker +=1												                    #if the password contains at least one symbol the counter will count it
	else:
		print '\tYou dont have at least one symbol'

	time.sleep(4)												                    #delay of 4 seconds
	
	print '\n \t \t \t SUCCESS!!!'
	print '\n\tYour password stands for the criteria of strong password \n'


ending=8														                      #counter for printing the end massage

while ending != 4:												                #loop for printing '>'
        print '>',
        sys.stdout.flush()
        time.sleep(.2)
        ending -= 1

time.sleep(.2)													                  #delay of 0.2 seconds
print 'End Of ',
sys.stdout.flush()												                #clearing the buffer
time.sleep(.4)												                    #delay of 0.4 seconds
print 'Complexity ',
sys.stdout.flush()												                #clearing the buffer
time.sleep(.4)													                  #delay of 0.4 seconds
print 'Check ',
sys.stdout.flush()												                #clearing the buffer
time.sleep(.2)													                  #delay of 0.2 seconds
            
while ending != 0:												                #loop for printing '<'
    	print '<',
    	sys.stdout.flush()
    	time.sleep(.2)
	ending -= 1
