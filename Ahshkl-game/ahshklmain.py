import ahshklterraingeneration as tege
import assets.bopas.ahshklbodyparts as bopas
import assets.objects.ahshklobjects as obje
import assets.bopas.ahshklbodypartsT2 as bopasT2
import assets.bopas.attributes.attributesMaterial as atmas

import time, sys


###Made by Sebastian W.###

bopa = bopas.bodyPart
bopasubsnames = ([bopasubc.__name__ for bopasubc in vars()['bopa'].__subclasses__()])
atma = atmas.MaterialAttributes
atmasubsnames = ([atmasubc.__name__ for atmasubc in vars()['atma'].__subclasses__()])

toCall = "ding-o"

toCall = raw_input("Please enter class name of object to test followed by name of atma to use (Help function activated by typing 'help'): ").lower()
toCall = toCall.split()
if 1:
	try:
		if toCall[0] == "help":
			print("List of bopas are as follows: " + str(bopasubsnames) + " and the atmas are: " + str(atmasubsnames))
			sys.exit("Exited with code 0")
		if toCall[0] == "enterdebug":
			toDo = raw_input("Welcome to debug. Please enter what you would like to do: ")
			try:
				print(eval(toDo))
				sys.exit("Exited with code 0")
			except NameError:
				print("Error! " + toDo + " is not defined! Check your spelling and make sure it exists!")
				sys.exit("Exited with code NameError")
			except AttributeError:
				print("Error! " + toDo[0] + " appears to not be a class! Check your spelling and make sure it exists!")
				sys.exit("Exited with code AttributeError")
		calling = getattr(bopas, toCall[0])
		callingatma = getattr(atmas, toCall[1])
		print("Welcome to the debug object parser interface. This is a demo of a " + calling.shapename + ". Caps have been added to all fields for emphasis. In normal gameplay it is capitalized properly.")
		calling.atma = callingatma.adjective
		sentence = ("There is a " + calling.sentencename.upper()  + " with codename of " + calling.codeName.upper() + ", a build ID of " + str(calling.bID) + ", a size unit of " + str(calling.size_unit) + ", and an atma of " + calling.atma.upper())
		time.sleep(1.5)
		print(sentence)
	except AttributeError:
		print("Error! Invalid class! Class '" + toCall[0] + "' or " + toCall[1] + "not found in file ahshklbodyparts.py or attributesMaterial.py, respectively")
		sys.exit("Exiting with code AttributeError")



print("Have a nice day!")
print("Exited with code 0")