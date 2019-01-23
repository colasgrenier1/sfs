"""
Executes
"""

from sfs.common import Error
import sfs.document as document
import sfs.parser as parser

class ExecutionError(Error):
	pass

class CommandNotFound(Error):
	pass

class State:
	"""
	A "State" contains for now command definitions,
	which can vary throughout the document and thua necessitate
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



class BlockCommand:
	"""
	Command that executes until a matching @end is received.

	This is to simplify block command construction: override the
	run() command in a subclass

	NOTE: this command preserves newline and space tokens.
	"""
	pass
	

def execute(doc, state, tokens):
	"""
	
	"""
	pass

