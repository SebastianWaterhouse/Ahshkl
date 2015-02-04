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
		calling = getattr(bopas, toCall)
		print("Welcome to the debug object parser interface. This is a demo of a " + getattr(bopas, toCall).shapename)
		sentence = ("There is " + calling.sentencename  + " with codename of " + calling.codeName + " and a build ID of " + str(calling.bID))
		print(sentence)
	except AttributeError:
		print("Error! Invalid class! Class '" + toCall + "' not found in " + str(bopas))
		sys.exit("Exiting with code 1")



print("Have a nice day!")
print("Exited with code 0")