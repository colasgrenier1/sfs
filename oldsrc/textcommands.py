"""
This file containes commands for text processing.
"""

import document
import executor

#Enable italic mode
def ATTR_i(doc, state, tokens):
	pass
i = executor.SimpleCommand(ATTR_i)

#Enable roman mode
def ATTR_r(doc, state, tokens):
	pass
r = executor.SimpleCommand(ATTR_r)

#Enable bold mode
def ATTR_b(doc, state, tokens):
	pass
b = executor.SimpleCommand(ATTR_b)

#Enable normal weight mode
def ATTR_n(doc, state, tokens):
	pass
n = executor.SimpleCommand(ATTR_n)










#Set font size
def CMD_fs(doc, state, tokens, *args):
	pass
fs = executor.SimpleCommand(CMD_fs)

#Set font name
def CMD_fn(doc, state, tokens, *args):
	pass
fn = executor.SimpleCommand(CMD_fn)








#
# Put text in center
#
def CMD_center(doc, state, tokens, *args):
	pass
center = executor.NumberedParameterCommand(1, CMD_center)



#
# Put text in italics
#
def CMD_ital(doc, state, tokens, *args):
	pass
ital = executor.NumberedParameterCommand(1, CMD_ital)

#
# Put text in bold
#
def CMD_bold(doc, state, tokens, *args):
	pass
bold = executor.NumberedParameterCommand(1, CMD_bold)



#
# New paragraph command
#
def CMD_newpar(doc, state):
	doc.newpar()
newpar = executor.SimpleCommand(CMD_newpar)
