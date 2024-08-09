#!/usr/bin/env python3

import sys

print(sys.version) # tells us the version of the python currently in use
print(sys.platform) # tells us our operating system platform
print(sys.argv) # tells us a list of all items given at the command line when running our python script from a command shell
print(len(sys.argv)) # tells us the number of command line arguments the user provide from a command shell
sys.exit() # will immediately end the running Python script, ignoring the remaining lines in the Python script

