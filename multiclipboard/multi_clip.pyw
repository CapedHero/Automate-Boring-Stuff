#!/usr/bin/env python3
#
# multi_clip.pyw - Saves and loads clipboard text from shelve file.
# Usage: <py> multi-clip.pyw save <keyword> - Saves clipboard text in keyword variable.
#        <py> multi-clip.pyw <keyword> - Loads clipboard text saved in keyword attribute.
#        <py> multi-clip.pyw list - Prints all keywords with corresponding saved clipboard text.
#
#        <py> = CLI reference to your python e.g.:
#               >>> python multi-clip.pyw list
#               OR
#               >>> python3 multi-clip.pyw list

import shelve
import sys

import pyperclip

multi_clip_shelf = shelve.open('mcb_shelf')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    multi_clip_shelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    if sys.argv[1] in multi_clip_shelf:
        pyperclip.copy(multi_clip_shelf[sys.argv[1]])

    elif sys.argv[1].lower() == 'list':
        for key in multi_clip_shelf.keys():
            print(key + ': ' + multi_clip_shelf[key])

multi_clip_shelf.close()
