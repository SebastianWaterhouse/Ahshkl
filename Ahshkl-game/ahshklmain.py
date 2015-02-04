import ahshklterraingeneration as tege
import assets.bopas.ahshklbodyparts as bopas
import assets.objects.ahshklobjects as obje
import assets.bopas.ahshklbodypartsT2 as bopasT2

import time


###Made by Sebastian W.###

bopa = bopas.bodyParts


toCall = "nein"

toCall = raw_input("Please enter class name of object to test: ")
print("Welcome to the debug object parser interface. This is a demo of " + toCall)
sentence = ("There is " + getattr(bopa, toCall).sentencename  + " with codename of " + getattr(bopa, toCall).codeName + " and a build ID of " + str(getattr(bopa, toCall).bID))
print(sentence)






print("Have a nice day!")
print("Exited with code 0")