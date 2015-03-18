"""
Depecrated command system, for future reference during The Switch
Sebastian W.
"""


	try:
		if command_split[0]=="help":
			success=1
			try:
				if command_split[1]=="help":
					print("Help gives a list of commands. To use help on a specific command, do help [command]")
				elif command_split[1]=="exit":
					print("Exit exits the game.")
				elif command_split[1]=="create":
					print("Create lets you enter a bopa that you would like to create. You can choose between pre-made bopas or make your own bopa.")
				elif command_split[1]=="interact":
					print("Interact lets you interact with a created object.")
				elif command_split[1]=="look":
					print("Look lets you see loaded bopas available for manipulation/interaction")
				elif command_split[1]=="destroy":
					print("Destroy lets you destroy a bopa. WARNING: This is final and if it is a custom bopa, you must enter all attributes all over again. SECOND WARNING: Does not destroy pre-built bopas!")
				else:
					print("Oops! That is not a valid command.")
			except IndexError:
				print("Commands are: help, exit, create, interact, look, destroy. Use help [command] for a detailed description of a command")
		if command_split[0]=="exit":
			sys.exit("Exited with code 0")
			success = 1
		if command_split[0]=="create":
			try:
				to_create_1 = command_split[1]
				try:
					to_create_2 = command_split[2]
					try:
						to_name = command_split[3]
					except IndexError as r:
						print("Continuing")
						raise r
				except IndexError as e:
					print("Continuing")
					done1 = True
					raise e
			except IndexError:
				if done1 == False:
					to_create_1=raw_input("Build your own (own) or use a prebuilt bopa (pre)?: ").lower()
			if to_create_1 == "pre":
				if to_create_2 == 'nil':
					to_create_2=raw_input("Which would you like? Say help for a list of bopas: ")
				if to_create_2=="help":
					for obj in gc.get_objects():
						if isinstance(obj, bopa):
							print(obj.shapename)
							success = 1
				if success == 0:
					if to_name == 'nil':
						to_name=raw_input("What do you want to name this?: ")
					exec(to_name + "=" + 'bopas.' + str(to_create_2))
			if to_create_1 == "own":
				to_create_2 = raw_input("Please enter the sentencename: ")
				to_create_4 = raw_input("Please enter the shapename: ")
				to_create_5 = raw_input("Please enter the size_unit: ")
				to_create_6 = raw_input("Please enter the atma: ")
				to_name = raw_input("Please name your bopa: ")
				exec(to_name + " = bopa('" + str(to_create_2) + "', '" + str(to_create_3) + "', '" + str(to_create_4) + "', '" + str(to_create_5) + "', '" + str(to_create_6) + "')")
			success = 1
		if command_split[0]=="interact":
			try:
				interact_with = command_split[1]
			except IndexError:
				interact_with=raw_input("Interact with ")
			finally:
				print("You interact with a " + getattr((eval(interact_with)), 'atma') + " " + getattr((eval(interact_with)), 'sentencename'))
			success = 1
		if command_split[0]=="no":
			print("What are you trying to accomplish by saying that?")
			success = 1
		if command_split[0]=="look":
			for obj in gc.get_objects():
				if isinstance(obj, bopa):
					print(obj.sentencename)
			success = 1
		if command_split[0]=="debug":
			if debug == False:
				debug = True
			else:
				debug = False
			print("Debug is now " + str(debug).upper())
			success = 1
		if command_split[0]=="destroy":
			try:
				to_destroy = command_split[1]
			except IndexError:
				to_destroy=raw_input("Destroy what?: ")
			destroying = eval(to_destroy)
			del destroying
			print(to_destroy + " destroyed successfully")
			success = 1
		if debug == True:
			if command_split[0]=="eval":
				try:
					print(eval(command_split[1]))
				except IndexError:
					print(eval(raw_input("Eval ")))
				success = 1
		if success==0:
			print("I don't know what you mean yet. Please file an issue ticket.")

		if success == 0:
			print("Oops! That was an invalid command. Please try again after The Switch.")
	except e:
		print("Oops! I don't know what that means yet. Please file an issue ticket.")
	to_create_2 = 'nil'
	to_name = 'nil'
	done1 = False