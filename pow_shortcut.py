# This sript is piping the passed value to the clipboard.

import os
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

# Add Zirkumflex
addToClipBoard('^')