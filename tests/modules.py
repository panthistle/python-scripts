
# ------------------------------------------------------------------------------
#
# ----------------------------- Importing --------------------------------------

# modules may be imported as follows:
#import sys
# python looks for modules in path directories
#print(sys.path)
# we can append different directories to the path or 
# (preferred) add the directory to environment variables

import random
# imported modules may be assigned a short handle
import modules_test_import as mti
# specific functions/variables may be imported from another module
#from imported_module import find_index, test
import time

def timed_output(msg, sep=' ', interval=1):
    l = msg.split(sep)
    for i in l:
        print(i)
        time.sleep(interval)

places = ['Athens', 'London', 'Paris', 'Rome']

# use imported module functions/variables
random_place = random.choice(places)
idx = mti.find_index(places, random_place)
print(random_place)
print(idx)
#print(mti.test)

# path to imported module
print(mti.__file__)

# function using imported module
timed_output('Sunday is the first day of the week')

