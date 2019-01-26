"""
Commands for paragraphs, sections.
"""

import document
import executor


#Space above paragraph
def CMD_sap(doc, state, *args):
	pass
sap = executor.NumberedParameterCommand(1, CMD_sap)

#Space below paragraph
def CMD_sbp(doc, state, *args):
	pass
sbp = executor.NumberedParameterCommand(1, CMD_sbp)

#Left pad
def CMD_lp(doc, state, *args):
	pass
lp = executor.NumberedParameterCommand(1, CMD_lp)

#Right pad
def CMD_rp(doc, state, *args):
	pass
rp = executor.NumberedParameterCommand(1, CMD_rp)

#Line spacing
def CMD_ls(doc, state, *args):
	pass
sbp = executor.NumberedParameterCommand(1, CMD_ls)
