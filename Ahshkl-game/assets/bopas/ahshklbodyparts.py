import attributes.attributesMaterial as atma

#WIP
class bodyPart(object):
	bID=-1
	sentencename="UNSET"
	codeName="UNSET"
	shapename="UNSET"
	size_unit = 0.5
	atma = "UNSET"
	def get_sentence_name(self):
		return self.sentencename
	def get_code_name(self):
		return self.codeName
	def get_shape_name(self):
		return self.shapename
	def get_build_ID(self):
		return self.bID
	def get_size_unit(self):
		return self.size_unit

class cylinder1(bodyPart):
	bID = 1
	sentencename = "cylinder"
	codeName = "smallCylinder1"
	shapename = "cylinder"
	size_unit = 0.5
class cube1(bodyPart):
	bID = 11
	sentencename = "small cube"
	codeName = "smallCube1"
	shapename = "cube"
	size_unit = 0.5
class sphere1(bodyPart):
	bID = 21
	sentencename = "small sphere"
	codeName = "smallSphere1"
	shapename = "sphere"
	size_unit = 0.5
class semicircle1(bodyPart):
	bID = 31
	sentencename = "small semi circle"
	codeName = "smallSemiCircle1"
	shapename = "semicircle"
	size_unit = 0.5
class square1(bodyPart):
	bID = 41
	sentencename = "small square"
	codeName = "smallSquare1"
	shapename = "square"
	size_unit = 0.5
class circle1(bodyPart):
	bID = 51
	sentencename = "small circle"
	codeName = "smallCircle1"
	shapename = "circle"
	size_unit = 0.5
class rectangle1(bodyPart):
	bID = 61
	sentencename = "small rectangle"
	codeName = "smallRectangle1"
	shapename = "rectangle"
	size_unit = 0.5