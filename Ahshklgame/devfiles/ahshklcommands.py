import time, sys, gc
import ahshklsettings as sett
import assets.main.bopas.ahshklbodyparts as bopas

#Created by Sebastian W.

class ahshklCommands():
	def debug():
		if sett.Debug == False:
			sett.Debug = True
		elif sett.Debug == True:
			sett.Debug = False
		print("Debug is now " + str(sett.Debug))
	def exit():
		sys.exit("Exited with code 0 (Command-Induced)")
		sett.sett.success = 1
	def look():
		for obj in gc.get_objects():
			if isinstance(obj, sett.bopa):
				print(obj.sentencename)
	def givemethebits():
		print("Bits? Here you go. END STEVEN UNIVERSE REFERENCE. BEGIN BITS TRANSMISSION: You want a cool game? Good! Then stay tuned here for a bit, but also check out Spacegame! Made by my friend Louis Goessling (github name), you can find it on github.")
	def helpp():
			try:
				if sett.command_split[1]=="help":
					print("Help gives a list of commands. To use help on a specific command, do help [command]")
				elif sett.command_split[1]=="exit":
					print("Exit exits the game.")
				elif sett.command_split[1]=="create":
					print("_DO_NOT_USE_MULTIPlE_ARGUMENTS!_ Create lets you enter a bopa that you would like to create. You can choose between pre-made bopas or make your own bopa.")
				elif sett.command_split[1]=="interact":
					print("_PREFIX_WITH_COMMS._ Interact lets you interact with a created object.")
				elif sett.command_split[1]=="look":
					print("Look lets you see loaded bopas available for manipulation/interaction")
				elif sett.command_split[1]=="destroy":
					print("_PREFIX_WITH_COMMS._ Destroy lets you destroy a bopa. WARNING: This is final and if it is a custom bopa, you must enter all attributes all over again. SECOND WARNING: Does not destroy pre-built bopas!")
				else:
					print("Oops! That is not a valid command.")
			except IndexError:
				print("Commands are: help, exit, create, interact, look, destroy. Use help [command] for a detcailed description of a command")
	def create():
		try:
			to_create_1 = sett.command_split[1]
			try:
				sett.to_create_2 = sett.command_split[2]
				try:
					sett.to_name = sett.command_split[3]
				except IndexError as a:
					print("Continuing")
					raise a
			except IndexError as b:
				print("Continuing")
				sett.done1 = True
				raise b
		except IndexError:
			if sett.done1 == False:
				sett.to_create_1=raw_input("Build your own (own) or use a prebuilt bopa (pre)?: ").lower()
		if sett.to_create_1 == "pre":
			if sett.to_create_2 == '':
				sett.to_create_2=raw_input("Which would you like? Say help for a list of bopas: ")
			if sett.to_create_2=="help":
				for obj in gc.get_objects():
					if isinstance(obj, sett.bopa):
						print(obj.shapename)
						sett.sett.success = 1
			if sett.success == 0:
				if sett.to_name == '':
					sett.to_name=raw_input("What do you want to name this?: ")
				exec(sett.to_name + "=" + 'bopas.' + str(sett.to_create_2))
		if sett.to_create_1 == "own":
			sett.to_create_2 = raw_input("Please enter the sentencename: ")
			sett.to_create_3 = raw_input("Please enter the shapename: ")
			sett.to_create_4 = raw_input("Please enter the size_unit: ")
			sett.to_create_5 = raw_input("Please enter the atma: ")
			sett.to_name = raw_input("Please name your bopa: ")
			exec(sett.to_name + " = bopa('" + str(sett.to_create_2) + "', '" + str(sett.to_create_3) + "', '" + str(sett.to_create_4) + "', '" + str(sett.to_create_5) + "')")
		sett.success = 1
	def interact():
		try:
			interact_with = sett.command_split[1]
		except IndexError:
			interact_with=raw_input("Interact with ")
		finally:
			print("You interact with a " + getattr((eval(interact_with)), 'atma') + " " + getattr((eval(interact_with)), 'sentencename'))
		sett.success = 1
	def destroy():
		if command_split[0]=="destroy":
			try:
				to_destroy = command_split[1]
			except IndexError:
				to_destroy=raw_input("Destroy what?: ")
			destroying = eval(to_destroy)
			del destroying
			print(to_destroy + " destroyed successfully")
			success = 1
	commands = {
	"look":look, "debug":debug, "exit":exit, "givemethe":givemethebits,
	"bits":givemethebits, "help":helpp, "create":create, "interact":interact,
	"destroy":destroy}
