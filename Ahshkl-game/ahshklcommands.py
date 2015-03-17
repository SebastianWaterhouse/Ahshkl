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
	if command_split[0]=="look":
		for obj in gc.get_objects():
			if isinstance(obj, bopa):
				print(obj.sentencename)
