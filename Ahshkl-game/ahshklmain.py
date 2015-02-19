import ahshklterraingeneration as tege
import assets.bopas.ahshklbodyparts as bopas
import assets.objects.ahshklobjects as obje
import assets.bopas.ahshklbodypartsT2 as bopasT2
import assets.bopas.attributes.attributesMaterial as atmas

import time, sys, gc


###Made by Sebastian W.###

bopa = bopas.bodyPart
bopasubsnames = ([bopasubc.__name__ for bopasubc in vars()['bopa'].__subclasses__()])
atma = atmas.MaterialAttributes
atmasubsnames = ([atmasubc.__name__ for atmasubc in vars()['atma'].__subclasses__()])
success=0
itemcount=1


print("Hi, welcome to Ahshkl. Please enter a command or enter help for a list of commands. Capitalization does not matter. Cube and sphere are pre-loaded in here by default under the names 'cube' and 'sphere', respectively.")
while 1:
	command=raw_input("Enter Command: ").lower()
	command_split=command.split()
	try:
		if command_split[0]=="help":
			success=1
			try:
				if command_split[1]=="help":
					print("Help gives a list of commands. To use help on a specific command, do help [command]")
				elif command_split[1]=="exit":
					print("Exit exits the game.")
				elif command_split[1]=="create":
					print("Create lets you enter a bopa that you would like to create, enter help to get a list of bopas.")
				elif command_split[1]=="interact":
					print("Interact lets you interact with a created object.")
				else:
					print("Oops! That is not a valid command.")
			except IndexError:
				print("Commands are: help, exit, create, interact. Use help [command] for a detailed description of a command")
		if command_split[0]=="exit":
			sys.exit("Exited with code 0")
			success = 1
		if command_split[0]=="create":
			to_create_1=raw_input("Build your own (own) or use a prebuilt bopa (pre)?: ").lower()
			if to_create_1 == "pre":
				to_create_2=raw_input("Which would you like? Say help for a list of bopas: ")
				if to_create_2=="help":
					for obj in gc.get_objects():
						if isinstance(obj, bopa):
							print(obj.shapename)
					success = 1
				if success == 0:
					to_name=raw_input("What do you want to name this?: ")
					exec(to_name + "=" + 'bopas.' + str(to_create_2))
			if to_create_1 == "own":
				to_create_2 = raw_input("Please enter the sentencename: ")
				to_create_3 = raw_input("Please enter the codeName: ")
				to_create_4 = raw_input("Please enter the shapename: ")
				to_create_5 = raw_input("Please enter the size_unit: ")
				to_create_6 = raw_input("Please enter the atma: ")
			success = 1
		if command_split[0]=="interact":
			interact_with=raw_input("Interact with ")
			print("You interact with a " + getattr(eval(interact_with), 'sentencename'))
			success = 1
		if command_split[0]=="no":
			print("What are you trying to accomplish by saying that?")
			success = 1
		if command_split[0]=="eval":
			print(eval(raw_input("Eval ")))
			success = 1
		if command_split[0]=="look":
			for obj in gc.get_objects():
				if isinstance(obj, bopa):
					print(obj.shapename)
		if success==0:
			print("I don't know what you mean yet. Please file an issue ticket.")
	except NameError:
		print("Oops! I don't know what that is yet! Please file an issue ticket.")
	except IndexError:
		pass
	success=0

print("Exited with code 0")