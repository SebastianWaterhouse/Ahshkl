import time, sys, gc
import ahshklsettings as sett

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
		success = 1
	def look():
		for obj in gc.get_objects():
			if isinstance(obj, sett.bopa):
				print(obj.sentencename)
	def givemethebits():
		print("Bits? Here you go. END STEVEN UNIVERSE REFERENCE. BEGIN BITS TRANSMISSION: You want a cool game? Good! Then stay tuned here for a bit, but also check out Spacegame! Made by my friend Louis Goessling (github name), you can find it on github.")
	def help():
			try:
				if command_split[1]=="help":
					print("Help gives a list of commands. To use help on a specific command, do help [command]")
				elif command_split[1]=="exit":
					print("Exit exits the game.")
				elif command_split[1]=="create":
					print("_CURRENTLY_DEPECRATED_ Create lets you enter a bopa that you would like to create. You can choose between pre-made bopas or make your own bopa.")
				elif command_split[1]=="interact":
					print("_CURRENTLY_DEPECRATED_ Interact lets you interact with a created object.")
				elif command_split[1]=="look":
					print("Look lets you see loaded bopas available for manipulation/interaction")
				elif command_split[1]=="destroy":
					print("_CURRENTLY_DEPECRATED_ Destroy lets you destroy a bopa. WARNING: This is final and if it is a custom bopa, you must enter all attributes all over again. SECOND WARNING: Does not destroy pre-built bopas!")
				else:
					print("Oops! That is not a valid command.")
			except IndexError:
				print("Commands are: help, exit, create, interact, look, destroy. Use help [command] for a detailed description of a command")
	commands = {
	"look":look, "debug":debug, "exit":exit, "givemethe":givemethebits,
	"bits":givemethebits, "help":help}