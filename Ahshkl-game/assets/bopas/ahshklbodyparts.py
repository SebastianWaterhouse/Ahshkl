#import

#WIP
class bodyPart(object):
	bID=-1
	sentencename="UNSET"
	codeName="UNSET"
	shapename="UNSET"
	def get_name(self):
		return self.sentencename

class cylinder1(bodyPart):
	bID = 1
	sentencename = "a cylinder"
	codeName = "smallCylinder1"
	shapename = "cylinder"
class cube1(bodyPart):
	bID = 11
	sentencename = "a small cube"
	codeName = "smallCube1"
	shapename = "cube"
class sphere1(bodyPart):
	bID = 21
	sentencename = "a small sphere"
	codeName = "smallSphere1"
	shapename = "sphere"
class semicircle1(bodyPart):
	bID = 31
	sentencename = "a small semi circle"
	codeName = "smallSemiCircle1"
	shapename = "semicircle"
class square1(bodyPart):
	bID = 41
	sentencename = "a small square"
	codeName = "smallSquare1"
	shapename = "square"
class circle1(bodyPart):
	bID = 51
	sentencename = "a small circle"
	codeName = "smallCircle1"
	shapename = "circle"
class rectangle1(bodyPart):
	bID = 61
	sentencename = "a small rectangle"
	codeName = "smallRectangle1"
	shapename = "rectangle"