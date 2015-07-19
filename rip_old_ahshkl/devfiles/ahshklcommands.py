import time, sys, gc, inspect
import ahshklsettings as sett
import assets.main.bopas.ahshklbodyparts as bopas
import ahshklplayer as play

#Created by Sebastian W.

class ahshklCommands(object):
	def debug():
		if sett.Debug == False:
			sett.Debug = True
		elif sett.Debug == True:
			sett.Debug = False
		print("Debug is now " + str(sett.Debug))
	def evalp():
		if sett.Debug == True:
			sett.to_eval = raw_input("Do what?: ")
			print(eval(sett.to_eval))
			print("Eval'd!")
		else:
			print("You do not have sufficient permission to run this command!")
		sett.success = 1
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
					print("_DO_NOT_USE_MULTIPlE_ARGUMENTS!_ Create lets you enter a bopa that you would like to create. Running the command will give you a list of everything you need to enter.")
				elif sett.command_split[1]=="interact":
					print("_PREFIX_WITH_COMMS._ Interact lets you interact with a created object.")
				elif sett.command_split[1]=="look":
					print("Look lets you see loaded bopas available for manipulation/interaction")
				elif sett.command_split[1]=="destroy":
					print("_PREFIX_WITH_COMMS._ Destroy lets you destroy a bopa. WARNING: This is final and if it is a custom bopa, you must enter all attributes all over again. SECOND WARNING: Does not destroy pre-built bopas!")
				elif sett.command_split[1]=="credits":
					print("")
				else:
					print("Oops! That is not a valid command.")
			except IndexError:
				print("Commands are: help, exit, create, interact, look, destroy, and credits. Use help [command] for a detcailed description of a command")
	def create():
		sett.to_create_2 = raw_input("Please enter the sentencename: ")
		sett.to_create_3 = raw_input("Please enter the shapename: ")
		sett.to_create_4 = raw_input("Please enter the size_unit: ")
		sett.to_create_5 = raw_input("Please enter the atma: ")
		sett.to_name = raw_input("Please name your bopa: ")
		exec(sett.to_name + " = sett.bopa('" + str(sett.to_create_2) + "', '" + str(sett.to_create_3) + "', '" + str(sett.to_create_4) + "', '" + str(sett.to_create_5) + "')")
		sett.success = 1
	def interact():
		interact_with=raw_input("Interact with ")
		print("You interact with a " + getattr(comms, eval(interact_with)).atma + " " + getattr(comms, eval(interact_with)).sentencename)
		sett.success = 1
	def destroy():
		to_destroy=raw_input("Destroy what?: ")
		to_destroy=("comms." + to_destroy)
		destroying = eval(to_destroy)
		del destroying
		print(to_destroy + " destroyed successfully")
		sett.success = 1
	def credits():
		print("Sebastian W.: Code, idea, creation, advertising, and everything else.")
	def buop():
		print("boup")
	commands = {
		"look":look, "debug":debug, "exit":exit, "givemethe":givemethebits,
		"bits":givemethebits, "help":helpp, "create":create, "interact":interact,
		"destroy":destroy, "credits":credits, "eval":evalp, "bees":buop}
