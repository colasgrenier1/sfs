"""







"""

from sfs.common import Error

class ParseError(Error):
	pass

class StreamReader:
	def __init__(self, fileobj):
		self.fileobj = fileobj
	def readchar(self):
		return self.fileobj.read(1)
	
class Newline:
	def __init__(self, content):
		self.content = content

class Space:
	def __init__(self, content):
		self.content = content

class Command:
	def __init__(self, name):
		self.name = name

class Word:
	def __init__(self, content):
		self.content = content

class Block:
	def __init__(self, content=None):
		if content:
			self.content = content
		else:
			self.content = []

def parse(stream):
	"""
	Returns a list of tokens
	"""
	tokens = []

	while True:
		c = stream.readchar()

		if not c:
			#We are at the end, return
			return tokens
		elif c == "\r":
			tokens.append(Newline("\r"))
		elif c == "\n":
			if tokens and type(tokens[-1]) is Newline and tokens[-1].content == "\r":
				tokens[-1].content = "\r\n"
			else:
				tokens.append(Newline("\n"))
		elif c in [' ', '\t']:
			if tokens and type(tokens[-1]) is Space:
				tokens[-1].content += c
			else:
				tokens.append(Space(c))
		elif c == "@":
			#If there are two consecutive @'s then it is an
			#escape for a single @ and not a command
			if tokens and type(tokens[-1]) is Command and len(tokens[-1].name) == 0:
				del tokens[-1]
				if tokens and type(tokens[-1]) is Word:
					tokens[-1].content += "@"
				else:
					tokens.append(Word("@"))
			else:
				tokens.append(Command(""))
		elif c == ";":
			#Semicolons can be used to end commands without adding spaces afterwards
			#We add a zero-length space
			#Otherwise it is treated as a letter in a word
			if tokens and type(tokens[-1]) is Command:
				tokens.append(Space(None))
			elif tokens and type(tokens[-1]) is Word:
				tokens[-1].content += c
			else:
				tokens.append(c)
		elif c == "<":
			#We append the contents of the block
			#The ending ">" should be taken up too
			tokens.append(Block(parse(stream)))
		elif c == ">":
			#we are supposed to be at the end of a brace here.
			return tokens
		else:
			#This is an ordinary character
			if tokens and type(tokens[-1]) is Word:
				tokens[-1].content += c
			#or part of a command name
			elif tokens and type(tokens[-1]) is Command:
				tokens[-1].name += c
			else:
				tokens.append(Word(c))


#Testing routines
if __name__ == "__main__":
	testscript = """allo comment ca va?@ital<allo moi aussi>
		mon email est unemail@@hotmail.com"""
	import io
	tokens = parse(StreamReader(io.StringIO(testscript)))

	def printout(toks, level=0):
		fmtstr = " "*level + "%-6s %s"
		for tok in toks:
			if type(tok) is Word:
				print(fmtstr % ("WORD", repr(tok.content)))
			elif type(tok) is Space:
				print(fmtstr % ("SPACE", repr(tok.content)))
			elif type(tok) is Command:
				print(fmtstr % ("CMD", tok.name))
			elif type(tok) is Newline:
				print(fmtstr % ("NEWL", repr(tok.content)))
			elif type(tok) is Block:
				print(fmtstr % ("BLOCK", (str(len(tok.content)) + " parts")))
				printout(tok.content, level+4)
			else:
				print("!!!!OTHER : " + str(type(tok)))

	printout(tokens)


