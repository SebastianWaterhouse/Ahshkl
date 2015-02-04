import ahshklterraingeneration as tege
import assets.bopas.ahshklbodyparts as bopas
import assets.objects.ahshklobjects as obje
import assets.bopas.ahshklbodypartsT2 as bopasT2

import time, sys


###Made by Sebastian W.###

bopa = bopas.bodyPart
bopasubsnames = ([bopasubc.__name__ for bopasubc in vars()['bopa'].__subclasses__()])

toCall = "ding-o"

toCall = raw_input("Please enter class name of object to test (Help function activated by typing 'help'): ")
if 1:
	try:
		if toCall == "help":
			print("List of bopas are as follows: " + str(bopasubsnames))
			sys.exit("Exited with code 0")
		print("Welcome to the debug object parser interface. This is a demo of a " + getattr(bopa, toCall).shapename)
		sentence = ("There is " + getattr(bopa, toCall).sentencename  + " with codename of " + getattr(bopa, toCall).codeName + " and a build ID of " + str(getattr(bopa, toCall).bID))
		print(sentence)
	except AttributeError:
		print("Error! Invalid class! Class '" + toCall + "' not found in class bodyParts")
		sys.exit("Exiting with code 1")






print("Have a nice day!")
print("Exited with code 0")