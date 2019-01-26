"""
Executes
"""

from sfs.common import Error
import sfs.document as document
import sfs.parser as parser

class CommandNotFound(Error):
	pass

class State:
	"""
	A "State" contains for now command definitions,
	which can vary throughout the document and thus necessitate
	a new data structure.
	"""

	def __init__(self, commands=None):
		if commands is not None:
			self.commands = commands.copy()
		else:
			self.commands = {}

	def set(self, name, command):
		"""

		"""
		self.commands[name] = command


	def resolve(self, name):
		"""
		Try to get the command object.
		"""
		if name in self.commands:
			return self.commands[name]
		else:
			raise CommandNotFound(str(name))

class Command:
	"""
	Base command class.
	"""
	pass

class SimpleCommand:
	"""
	Simple command.
	"""
	def __init__(self, run=None):
		self.run = run

	def run(self, doc, state, args):
		pass

class NumberedParameterCommand:
	"""
	Command that takes in only a fixed number of paramreters.

	This is to allow simpler command construction: the only
	thing needed is to subclass the run() command or to pass
	it as an argument to the constructor.

	NOTE: this command removes direct space and fails if there
	are not enough tokens on the line.
	"""
	def __init__(self, nargs, run=None):
		self.nargs = nargs
		if run is not None:
			self.run = run

	def run(self, doc, state, *args):
		"""
		Subclass this.
		"""
		pass

	def execute(self, doc, state, tokens):
		#We try to eat up as many arguments as we need.
		#skipping spaces, failing on newline
		count = 0
		while count < self.nargs:
			tok = tokens.pop(0)
			if type(tok) is parser.Space:
				pass
			elif type(tok) is parser.Newline:
				raise Exception("COMMAND %s DID NOT RECEIVE ENOUGH ARGUMENTS UNTIL NEWLINE!" % (tok.name,))
			elif type(tok) is parser.Word:
				pass
			elif type(tok) is parser.Block:
				pass
			elif type(tok) is parser.Command:
				pass
			else:
				raise Error()

class BlockCommand:
	"""
	Command that executes until a matching @end is received.

	This is to simplify block command construction: override the
	run() command in a subclass

	NOTE: this command preserves newline and space tokens.
	"""

	def run(self, doc, state, content):
		"""
		This function exeutes with the tokens contained
		between the invocation and @end
		"""
		pass

	def execute(self, doc, state, tokens):
		pass




def execute(doc, state, tokens):
	"""
	Execute on a sttring of tokens.

	Essentially this adds to the document....
	"""
	#We execute on all tokens
	while tokens:

		#We take in a token
		tok = tokens.pop(0)

		if tok.type == "word":
			
