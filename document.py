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

class LineBreak:
	"""
	This is the child of a Text object.
	"""
	pass
		
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
	If not broken and if column configuration is the same, and if
	margins, etc. are the same, it is possible
	that there will be multiple sections on the same page. In this case
	the header/footer information will be that of the last section to be
	configured on that page.
	
	The headers and the footers must be Paragraph objects, with the
	known escape sequences.
	"""
	def __init__(self,
		break = False, #Whether to start this section on a new page
		columns = 1, #Number of columns
		column_separation = None, #Space between columns
		column_flush = False, #Wether to make the end of two columns flush (like \multicol and not \multicol*)
		margin_top =
		margin_bottom = 
		margin_left_even =
		margin_left_odd = 
		margin_right_even = 
		margin_right_odd =
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
