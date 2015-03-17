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
		sys.exit("Exited with code 0")
		success = 1
	def look():
		for obj in gc.get_objects():
			if isinstance(obj, sett.bopa):
				print(obj.sentencename)
	commands = {"look":look, "debug":debug, "exit":exit}