import ahshklterraingeneration as tege
import ahshklbodyparts as bopa
import ahshklobjects as obje
import time


goto = raw_input("Do you want to access tege, bopa, or obje? ")
if goto == "tege":
	selffile = tege
	print("Nothing here for now!")
if goto == "bopa":
	selffile = bopa.bodyParts
	bopaToAccess = raw_input("What body part do you want? ")
	if bopaToAccess == "getList":
		print(str(selffile.__subclasses__()))
	if bopaToAccess in str(selffile.__subclasses__()):
		selfbopa = selffile.toAccess
		print("You have accessed" + str(selfbopa))
if goto == "obje":
	print("Nothing here for now!")





print("Have a nice day!")