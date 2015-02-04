import ahshklterraingeneration as tege
import assets.bopas.ahshklbodyparts as bopas
import assets.objects.ahshklobjects as obje
import assets.bopas.ahshklbodypartsT2 as bopasT2

import time, sys


###Made by Sebastian W.###

bopa = bopas.bodyParts


toCall = "ding-o"

toCall = raw_input("Please enter class name of object to test (Help function WIP): "
if 1:
	try:
		print("Welcome to the debug object parser interface. This is a demo of a " + getattr(bopa, toCall).shapename)
		sentence = ("There is " + getattr(bopa, toCall).sentencename  + " with codename of " + getattr(bopa, toCall).codeName + " and a build ID of " + str(getattr(bopa, toCall).bID))
		print(sentence)
	except AttributeError:
		print("Error! Invalid class! Class '" + toCall + "' not found in class bodyParts")
		sys.exit("Exiting with code 1")






print("Have a nice day!")
print("Exited with code 0")