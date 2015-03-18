import ahshklterraingeneration as tege
import ahshklcommands as comms
import ahshklsettings as sett
import assets.main.bopas.ahshklbodyparts as bopas
import assets.main.objects.ahshklobjects as obje
import assets.main.bopas.ahshklbodypartsT2 as bopasT2
import assets.main.bopas.attributes.attributesMaterial as atmas
from assets.mods import * as mods

import time, sys, gc


###Made by Sebastian W.###

sett.init()

to_create_2 = 'nil'
to_name = 'nil'
commands = comms.ahshklCommands.commands
modmands = mods.ahshklCommands.commands
e = NameError
d = IndexError
c = KeyboardInterrupt

sett.Debug = False

print("Welcome to Ahshkl! Currently going through The Switch. Please read README.")
while 1:
	command=raw_input("Enter Command: ").lower()
	command_split=command.split()
	try:
		if command_split[0] in modmands:
			commands[str(command_split[0])]()
			success = 1
	try:
		if command_split[0] in commands:
			commands[str(command_split[0])]()
			success = 1
		if success == 0:
			print("Oops! That was an invalid command. Please try again after The Switch.")
	except e:
		print("Oops! I don't know what that means yet. Please try again after The Switch.")
	except d:
		pass
	except c:
		sys.exit("Exited with code 0.5 (KeyboardInterrupt)")
	success=0

print("Exited with code 0")