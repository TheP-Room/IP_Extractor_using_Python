#!/bin/python3

import subprocess

# following function is just for easy visibility
def separating():
	print('===================================')

# following function is for guiding the user for using the program
# contains simple input data
def guiding():
	separating()
	print("Example of Domain Name : google.com")
	separating()
	f = input("DOMAIN NAME: ")
	if (f == ''):
		separating()
		print("Do not Leave it Empty!")
		guiding()
	else:
		the_command(f)

# following function ask user for continue resolving or not
def further_continue():
	g = input("Try More? (y/n): ")
	if (g == 'y'):
		guiding()
	elif (g == 'n'):
		separating()
		print("Okk Bye!")
		separating()
	else:
		separating()
		print("I Think NO! Byee!")
		separating()

# following function is the main part where the code happens
def the_command(a):
# subprocess.popen -- used to run and wait for the command with pipe to execute
	b = subprocess.Popen(('nslookup','{}'.format(a), '-query=hinfo'), stdout=subprocess.PIPE)
# subprocess.check_output -- let us store the output in variable
# subprocess.run -- also let us store the output in variable but also itself prints the output
	c = subprocess.check_output(('grep', '-w', 'Address'), stdin=b.stdout)
	d = str(c)
# using split to convert string output in list format
	e = d.split("\\n")
	e.pop()
	del e[0]
	if (len(e) == 0):
		separating()
		print('Not Valid! or Server Down!')
		guiding()
	else:
		separating()
		for j in e:
			print(j)
		separating()
		further_continue()

guiding()
