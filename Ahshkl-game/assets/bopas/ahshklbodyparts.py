import attributes.attributesMaterial as atma
import weakref

#WIP
class bodyPart(object):
	prebuiltbopas = []
	def __init__(self, sentencename="UNSET", codeName="UNSET", shapename="UNSET", size_unit="UNSET", atma="UNSET"):
		self.sentencename= sentencename
		self.codeName= codeName
		self.shapename= shapename
		self.size_unit = size_unit
		self.atma = atma
		self.__class__.prebuiltbopas.append(weakref.ref(self))
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

cube = bodyPart("cube", "cube1", "cube", "1", "UNSET")
sphere = bodyPart("sphere", "sphere1", "sphere", "1", "UNSET")
