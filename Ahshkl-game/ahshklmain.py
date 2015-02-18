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
itemcount=0

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
				print("Create lets you enter a bopa that you would like to create, enter help to get a list of bopas.")
			else:
				print("Oops! That is not a valid command.")
		except IndexError:
			print("Commands are: help, exit, create. Use help [command] for a detailed description of a command")
	if command_split[0]=="exit":
		sys.exit("Exited with code 0")
		success = 1
	if command_split[0]=="create":
		to_create=raw_input("Create a ")
		if to_create == "help":
			print("Bopas are: " + str(bopasubsnames))
			success = 1
		if success == 0:
			try:
				print("You create a " + getattr(bopas, to_create).sentencename)
				exec('item'+str(itemcount) + '= getattr(bopas, to_create)')
				itemcount = itemcount+1
			except AttributeError:
				print("Oops! " + to_create + " is not a valid bopa.")
			success = 1
	if command_split[0]=="interact":
		interact_with=raw_input("Interact with ")
		print("You interact with a " + getattr(eval(interact_with), 'sentencename'))
	if command_split[0]=="no":
		print("What are you trying to accomplish by saying that?")
		success = 1
	if command_split[0]=="eval":
		print(eval(raw_input("Eval ")))
	if success==0:
		print("I don't know what you mean yet. Please file an issue ticket.")
	success=0

print("Exited with code 0")