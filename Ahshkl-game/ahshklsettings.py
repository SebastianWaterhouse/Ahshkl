import ahshklterraingeneration as tege
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