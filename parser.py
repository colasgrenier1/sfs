
(No subject)
Nicolas Grenier
Today, 12:56 PMNicolas Grenier

"""







"""



class StreamReader:
    def __init__(self, fileobj):
        self.fileobj fileobj
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

        if c == "\r":
            tokens.append(Newline("\r"))
        elif c == "\n":
            if tokens and tokens[-1] is Newline and tokens[-1].content == "\r":
                tokens[-1].content = "\r\n"
            else:
                tokens.append(Newline("\n"))
        elif c in [' ', '\t']:
            if tokens and tokens[-1] is Space:
                tokens[-1].content.append(c)
            else:
                tokens.apend(Space(c))
        elif c == "@":
            tokens.append(Command(""))
        eli c == ";"
     
