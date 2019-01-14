"""
Document Container
"""

UNITS = ["cm", "in", "pt"]

UNIT_EQUIVALENCE = {
	"cm" : {
			"in" : 0.393701,
			"cm" : 1,
			"pt" : 28.3465
		},
	"in" : {
			"in" : 1,
			"cm" : 2.54,
			"pt" : 71
		}
	"pt" : {
			"cm" : 0.0352778,
			"in" : 0.0138889,
			"pt" : 1
		}
}

class Value:
	def __init__(self, value, unit):
		self.value = value
		self._unit = None
		self.unit = unit
		
	@property
	def unit(self):
		return self.unit
	
	@unit.set
	def set_unit(self, unit):
		if unit not in UNITS:
			raise Exception("Allowed units are : " + ', '.join(UNITS))

	def get(self, unit=None):
		if unit is None:
			return self.value
		else:
			return self.value * UNIT_EQUIVALENCE[self.unit][unit]

class Character:
	"""
	This is a child of a Text object.
	"""
	def __init__(self, char):
		self.char = char

class Space:
	"""
	This is a child of a Text object.
	"""
	def __init__(self, breaking=True, width=None):
		self.breaking = breaking

class Text:
	pass

class Image:
	pass

class Link:
	pass
	
class Paragraph:
	"""
	This is a collection of document objects (such as the ones above).
	"""
	pass
	
class Section:
	"""
	A section is a collection of paragraphs, and contains stable
	page format and header format etc.
	"""
	def __init__(self,
		page_height = LETTER_HEIGHT,
		page_width = LETTER_WIDTH,
		page_orientation = "portrait"
	):
	
class Document:
	"""
	A document is the highest level entity. It contains sections.
	"""
	def __init__(self,
		name =  None
		):
		self.name = name
