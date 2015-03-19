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

def resetVars():
	sett.done1 = False
	sett.success = 0
	sett.to_create_1 = ''
	sett.to_create_2 = ''
	sett.to_create_3 = ''
	sett.to_create_4 = ''
	sett.to_create_5 = ''
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
	except sett.e:
		"Oops! I don't know what that means! Please try again after The Switch."
	except sett.d:
		pass
	except sett.c:
		sys.exit("Exited with code 0.5 (KeyboardInterrupt)")
	resetVars()

print("Exited with code 0")
