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
			"pt" : 72
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
		self.background_color = background_color


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
class Link:
	pass

class Footnote:
	pass

class Image:
	pass

class Equation:
	pass

class MarginText:
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


class Document:
	"""
	A document is the highest level entity. It contains paragraphs
	for now but will eventually include sections.
	"""
	def __init__(self,
		name =  None
		):
		self.name = name

		self.sections = []

	def newpar(self, parconf=None):
		"""
		Creates a new paragraph with the same style as the previous or new one.
		"""

		##If we do not have a section we create one
		#if not self.sections:
		#	self.newsec()

		#We create the parapraph
		self.paragraphs.append(Paragraph())

		#We set the style according to the specifications
		if parconf is not None:
			self..paragraphs[-1].configuration = parconf
		else:
			# #We search for the last paragraph
			# for sec in reversed(self.sections):
			# 	if sec.paragraphs:
			# 		self.sections[-1].paragraphs[-1].configuration = sec.paragraphs[1].configuration
			# 		break
			# 	else:
			# 		#We did not have a P so
			# 		self.sections[-1].paragraphs[-1].configuration = ParagraphConfiguration()
			if self.paragraphs[:-1]:
				self.paragraphs[-1].configuration = self.paragraphs[-2].configuration
			else:
				self.paragraphs[-1].configuration = ParagraphConfiguration()

	#def newsec(self, secconf=None):
	#	"""
	#	Creates a new section with the same style as the previous.
	#	"""
	#	Section
