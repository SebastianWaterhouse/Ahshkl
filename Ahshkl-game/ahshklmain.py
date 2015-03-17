import ahshklterraingeneration as tege
import ahshklcommands as comms
import assets.main.bopas.ahshklbodyparts as bopas
import assets.main.objects.ahshklobjects as obje
import assets.main.bopas.ahshklbodypartsT2 as bopasT2
import assets.main.bopas.attributes.attributesMaterial as atmas

import time, sys, gc


###Made by Sebastian W.###

bopa = bopas.bodyPart
bopasubsnames = ([bopasubc.__name__ for bopasubc in vars()['bopa'].__subclasses__()])
atma = atmas.MaterialAttributes
atmasubsnames = ([atmasubc.__name__ for atmasubc in vars()['atma'].__subclasses__()])
success=0
itemcount=1
debug = False
cube = bopas.cube
sphere = bopas.sphere
to_create_2 = 'nil'
to_name = 'nil'
e = NameError


print("Hi, welcome to Ahshkl. Please enter a command or enter help for a list of commands. Capitalization does not matter. Cube and sphere are pre-loaded in here by default under the names 'cube' and 'sphere', respectively.")
while 1:
	command=raw_input("Enter Command: ").lower()
	command_split=command.split()
	try:
		print("Hello! The Switch (refer to README for information) is in it's awkward stage. Nothing currently works. Come back next commit for extremely limited functionality!")
		sys.exit("Exited with code 0")
		success = 1
		if success == 0:
			print("Oops! That was an invalid command. Please try again after The Switch.")
	except e:
		print("Oops! I don't know what that means yet. Please file an issue ticket.")
	except IndexError:
		pass
	to_create_2 = 'nil'
	to_name = 'nil'
	done1 = False
	success=0

print("Exited with code 0")