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
	"""
	Generic value, must be in cm. in. or pt.
	"""
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

class Color:
	"""
	Generic color class.
	Now in RGB format only.
	"""
	def __init__(self, R, G, B):
		self.R = R
		self.G = G
		self.B = B

class TextConfiguration:
	"""
	Text configuration object.
	"""
	def __init__(
		self,
		alignment = "left",
		font_name = None,
		font_size = None,
		font_style = "roman",
		font_weight = "normal"
		color = None,
		background_color = None,
		):

		self.alignment = alignment
		self.font_name = font_name
		self.font_size = font_size
		self.font_style = font_style
		self.font_weight = font_weight
		self.color = color
		self.background_color
		

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
	"""
	Contains text of one style.

	It is a list of characters, spaces, line breaks, etc.
	"""
	def __init__(self, content=None, style=None):

		#Content is a list of characters, spaces, etc.
		if content is None:
			self.content = content
		else:
			self.content = []

		#We set the style of this text
		#If none we set the default style (empty values)
		if style is None:
			self.style = TextConfiguration()
		else:
			self.style = style

class Image:
	pass

class Link:
	pass

class ParagraphConfiguration:
	def __init__(self,
		above = None,
		below = None,
		left = None,
		right = None
		line_spacing = None,
		):

		self.above = None
		self.below = None
		self.left = None
		self.right = None
		self.line_spacing = None
		
		
class Paragraph:
	"""
	This is a collection of document objects (such as the ones above).
	"""
	def __init__(self, contents=None):
		if contents is None:
			self.contents = []
		else:
			self.contents = contents

class PageBreak:
	"""
	Breaks a page, but keeps the same section
	"""
	pass
	
class Section:
	"""
	A section is a collection of paragraphs (and page breaks, etc.),
	and contains stable page format and header format etc.
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

		self.paragraphs = []

	):
	
class Document:
	"""
	A document is the highest level entity. It contains sections.
	"""
	def __init__(self,
		name =  None
		):
		self.name = name

		self.sections = []
