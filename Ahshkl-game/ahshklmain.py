import ahshklterraingeneration as tege
import ahshklcommands as comms
import ahshklsettings as sett
import assets.main.bopas.ahshklbodyparts as bopas
import assets.main.objects.ahshklobjects as obje
import assets.main.bopas.ahshklbodypartsT2 as bopasT2
import assets.main.bopas.attributes.attributesMaterial as atmas

import time, sys, gc


###Made by Sebastian W.###

sett.init()

to_create_2 = 'nil'
to_name = 'nil'
commands = comms.ahshklCommands.commands
e = NameError
d = IndexError

sett.Debug = False

while 1:
	command=raw_input("Enter Command: ").lower()
	command_split=command.split()
	try:
		if command in commands:
			commands[str(command)]()
			success = 1
	except IndexError:
		pass
	success=0

print("Exited with code 0")