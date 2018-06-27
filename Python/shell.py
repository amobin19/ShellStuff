import os
import sys
while(True):
	command = input("Command: ")
	if(command == "exit"):
		break;
	elif(command == "pwd"):
		print(os.getcwd())
	elif(command == "ls"):
		print(os.listdir(os.getcwd()))
	else:
		print("Error invalid input")