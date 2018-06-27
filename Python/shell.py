import os

while(True):
	command = input("Command: ")
	if(command == "exit"):
		break;
	elif(command == "pwd"):
		print(os.getcwd())
	elif(command == "ls"):
		print(os.listdir(os.getcwd()))
	elif(command[0:2] == "cd"):
		if(os.path.isdir(command[3:])):
			os.chdir(command[3:])
		elif(command[3:] == "--"):
			os.chdir("/root/")
		else:
			print("Error directory does not exist")
	else:
		print("Error invalid input")