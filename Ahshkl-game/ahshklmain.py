import ahshklterraingeneration as tege
import assets.bopas.ahshklbodyparts as bopas
import assets.objects.ahshklobjects as obje
import assets.bopas.ahshklbodypartsT2 as bopasT2
import assets.bopas.attributes.attributesMaterial as atmas

import time, sys


###Made by Sebastian W.###

bopa = bopas.bodyPart
bopasubsnames = ([bopasubc.__name__ for bopasubc in vars()['bopa'].__subclasses__()])
atma = atmas.MaterialAttributes
atmasubsnames = ([atmasubc.__name__ for atmasubc in vars()['atma'].__subclasses__()])
success=0

print("Hi, welcome to Ahshkl. Please enter a command or enter help for a list of commands. Capitalization does not matter.")
while 1:
	command=raw_input("Enter Command: ").lower()
	command_split=command.split()
	if command_split[0]=="help":
		success=1
		try:
			if command_split[1]=="help":
				print("Help gives a list of commands. To use help on a specific command, do help [command]")
			elif command_split[1]=="exit":
				print("Exit exits the game.")
			elif command_split[1]=="create":
				print("Create is not yet implemented")
			else:
				print("Oops! That is not a valid command.")
		except IndexError:
			print("Commands are: help, exit, create. Use help [command] for a detailed description of a command")
	if command_split[0]=="exit":
		sys.exit("Exited with code 0")
		success = 1
	if command_split[0]=="create":
		print("Create is not yet implemented. Please try again in next version.")
		success = 1
	if success==0:
		print("I don't know what you mean yet. Please file an issue ticket.")
	success=0

print("Exited with code 0")