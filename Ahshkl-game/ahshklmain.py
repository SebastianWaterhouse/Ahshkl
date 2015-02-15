import ahshklterraingeneration as tege
import assets.bopas.ahshklbodyparts as bopas
import assets.objects.ahshklobjects as obje
import assets.bopas.ahshklbodypartsT2 as bopasT2

import time, sys


###Made by Sebastian W.###

bopa = bopas.bodyPart
bopasubsnames = ([bopasubc.__name__ for bopasubc in vars()['bopa'].__subclasses__()])

toCall = "ding-o"

toCall = raw_input("Please enter class name of object to test (Help function activated by typing 'help'): ").lower()
if 1:
	try:
		if toCall == "help":
			print("List of bopas are as follows: " + str(bopasubsnames))
			sys.exit("Exited with code 0")
		if toCall == "enterdebug":
			toDo = raw_input("Welcome to debug. Please enter what you would like to do: ")
			try:
				print(eval(toDo))
				sys.exit("Exited with code 0")
			except NameError:
				print("Error! " + toDo + " is not defined! Check your spelling and make sure it exists!")
				sys.exit("Exited with code NameError")
			except AttributeError:
				print("Error! " + toDo + " appears to not exist! Check your spelling and make sure it exists!")
				sys.exit("Exited with code AttributeError")
		calling = getattr(bopas, toCall)
		print("Welcome to the debug object parser interface. This is a demo of a " + calling.shapename + ". Caps have been added to all fields for emphasis. In normal gameplay it is capitalized properly.")
		sentence = ("There is a " + calling.sentencename.upper()  + " with codename of " + calling.codeName.upper() + ", a build ID of " + str(calling.bID) + " and a size unit of " + str(calling.size_unit))
		time.sleep(4)
		print(sentence)
	except AttributeError:
		print("Error! Invalid class! Class '" + toCall + "' not found in file ahshklbodyparts.py")
		sys.exit("Exiting with code AttributeError")



print("Have a nice day!")
print("Exited with code 0")