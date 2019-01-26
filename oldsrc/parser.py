"""







"""

class StreamReader:
	def __init__(self, fileobj):
		self.fileobj = fileobj
	def readchar(self):
		return self.fileobj.read(1)

class Token:
	def __init__(self, type, content):
		self.type = type
		self.content = content

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
			tokens.append(Token("newline", "\r"))
		elif c == "\n":
			if tokens and tokens[-1].type=="newline" and tokens[-1].content == "\r":
				tokens[-1].content = "\r\n"
			else:
				tokens.append(Token("newline", "\n"))
		elif c in [' ', '\t']:
			if tokens and tokens[-1].type=="space":
				tokens[-1].content += c
			else:
				tokens.append(Token("space", c))
		elif c == "@":
			#If there are two consecutive @'s then it is an
			#escape for a single @ and not a command
			if tokens and tokens[-1].type == "command" and len(tokens[-1].content) == 0:
				del tokens[-1]
				if tokens and tokens[-1].type == "word":
					tokens[-1].content += "@"
				else:
					tokens.append(Token("word", "@"))
			else:
				tokens.append(Token("command", ""))
		elif c == ";":
			#Semicolons can be used to end commands without adding spaces afterwards
			#We add a zero-length space
			#Otherwise it is treated as a letter in a word
			if tokens and tokens[-1].type == "command":
				tokens.append(Token("empty", None))
			elif tokens and tokens[-1].type == "word":
				tokens[-1].content += c
			else:
				tokens.append(c)
		elif c == "<":
			#We append the contents of the block
			#The ending ">" should be taken up too
			tokens.append(Token("block", parse(stream)))
		elif c == ">":
			#we are supposed to be at the end of a brace here.
			return tokens
		else:
			#This is an ordinary character
			if tokens and tokens[-1].type == "word":
				tokens[-1].content += c
			#or part of a command name
			elif tokens and tokens[-1].type == "command":
				tokens[-1].content += c
			else:
				tokens.append(Token("word", c))


#Testing routines
if __name__ == "__main__":
	testscript = """allo comment ca va?@ital<allo moi aussi>
		mon email est unemail@@hotmail.com

		@ital<@bold<@emph<allo comment moi aussi @i @n @r>>@aolle<>>

		DIPLODOCUS
		"""
	import io
	tokens = parse(StreamReader(io.StringIO(testscript)))

	def printout(toks, level=0):
		fmtstr = " "*level + "%-6s %s"
		for tok in toks:
			if tok.type == "word":
				print(fmtstr % ("WORD", repr(tok.content)))
			elif tok.type == "space":
				print(fmtstr % ("SPACE", repr(tok.content)))
			elif tok.type == "command":
				print(fmtstr % ("CMD", tok.content))
			elif tok.type == "newline":
				print(fmtstr % ("NEWL", repr(tok.content)))
			elif tok.type == "block":
				print(fmtstr % ("BLOCK", (str(len(tok.content)) + " parts")))
				printout(tok.content, level+4)
			else:
				print("!!!!OTHER : " + str(tok.type))

	printout(tokens)
