# Written by Ayman Mobin
import os

while(True):
	command = input("Command: ")
	
	#INTERNAL
	if(command == "exit"): # exit
		break;
	elif(command == "pwd"): # print working directory
		print(os.getcwd())
	elif(command == "ls"): # list
		print(os.listdir(os.getcwd()))
	elif(command[0:2] == "cd"): # change directory
		if(os.path.isdir(command[3:])):
			os.chdir(command[3:])
		elif(command[3:] == "--"): # change to root directory
			os.chdir("/root/")
		else: # non existent directory
			print("Error directory does not exist")
	
	# EXTERNAL
	else: 
		if(os.system(command) != 0): # invalid external argument
			print("Error invalid argument")
		else: # execution of external argument
			os.system(command)