import ahshklcommands as comms
import assets.main.bopas.ahshklbodyparts as bopas
import assets.main.bopas.attributes.attributesMaterial as atmas
import assets.mods

def init():
	global Debug
	Debug = False
	global bopa
	bopa = bopas.bodyPart
	global atma
	atma = atmas.MaterialAttributes
	global cube
	cube = bopas.cube
	global sphere
	sphere = bopas.sphere
	global mods
	mods = assets.mods
	global success
	success = 0
	global command_split
	command_split = []
	global done1
	done1 = False
	global to_create_1
	to_create_1 = ''
	global to_create_2
	to_create_2 = ''
	global to_create_3
	to_create_3 = ''
	global to_create_4
	to_create_4 = ''
	global to_create_5
	to_create_5 = ''
	global to_name
	to_name = ''
	global e
	e = NameError
	global d
	d = IndexError
	global c
	c = KeyboardInterrupt
