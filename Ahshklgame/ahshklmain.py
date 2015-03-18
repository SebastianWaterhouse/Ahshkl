import devfiles.ahshklterraingeneration as tege
import devfiles.ahshklcommands as comms
import devfiles.ahshklsettings as sett
import devfiles.assets.main.bopas.ahshklbodyparts as bopas
import devfiles.assets.main.objects.ahshklobjects as obje
import devfiles.assets.main.bopas.ahshklbodypartsT2 as bopasT2
import devfiles.assets.main.bopas.attributes.attributesMaterial as atmas
import devfiles.assets.mods.ahshklmod as mods

import time, sys, gc


###Made by Sebastian W.###

sett.init()

commands = comms.ahshklCommands.commands
modmands = mods.modCommands.commands
e = NameError
d = IndexError
c = KeyboardInterrupt

def resetVars():
	sett.done1 = False
	success = 0
	to_create_2 = ''
	to_name = ''

print("Welcome to Ahshkl! Currently going through The Switch. Please read README.")
while 1:
	command=raw_input("Enter Command: ").lower()
	sett.command_split=command.split()
	try:
		if sett.command_split[0] in modmands:
			modmands[str(sett.command_split[0])]()
			sett.success = 1
		if sett.success == 0:
			if sett.command_split[0] in commands:
				commands[str(sett.command_split[0])]()
				sett.success = 1
		if sett.success == 0:
			print("Oops! That was an invalid command. Please try again after The Switch.")
	except d:
		pass
	except c:
		sys.exit("Exited with code 0.5 (KeyboardInterrupt)")
	resetVars()

print("Exited with code 0")
