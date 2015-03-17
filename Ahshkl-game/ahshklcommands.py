import time, sys, gc

#Created by Sebastian W.

class ahshklCommands():
	def exit():
		sys.exit("Exited with code 0")
		success = 1
	def debug():
		if Debug == False:
			Debug = True
		elif Debug == True:
			Debug = False
		print("Debug is now " + str(Debug))
