import ahshklsettings as sett
import assets.mods as mods
import sys, os

def findall(directoryname=".assets/mods"):
	end = '.py'
	for root, dirs, files in os.walk(directoryname):
	    for name in files:
	    	if
	        print(os.path.join(root, name))
