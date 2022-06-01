
# ------------------------------------------------------------------------------
#
# ------------------------------ Strings ---------------------------------------

# str variable
s = 'hello'
# in quotes
s = '"hello"' # OR "'hello'"

s = 'another message'
# number of characters (string length)
lct = len(s)
# sub-strings
sub = s[5]          # 5th character
sub = s[0:6]        # first 5 characters
sub = s[:5]         # first 4 characters
sub = s[-4:-2]      # 2 characters before end
sub = s[:-1]        # all characters except last

# convert to upper/lower case
S = s.upper()
s = S.lower()

nsub = s.count('e') # number of occurrences of substring
isub = s.find('e')  # index of first occurrence of substring

# replace a portion of string
s = s.replace('another', 'new')
p = 'John'
# combine strings
greeting = f'{s} for {p.upper()}'

# python str object methods
#print(dir(s))

# help on python str object
#print(help(str))



# ------------------------------------------------------------------------------
#
# ------------------------------- Lists ----------------------------------------

# new list object
lst = []
lst = list()

l = [1, 3, 5, 7]

lct = len(l)            # number of items (list length)
itm = l[2]              # access index 2 - third item
itm = l[-1]             # access last item
sub = l[0:3]            # sublist of first 3 items

l.append(9)             # append new item at end of list
n = 11
l.insert(2, n)         	# insert new item at specific index

l2 = [20, 30]
l.insert(0, l2)			# insert another list object at specified index
l.extend(l2)			# append all items of one list at end of another
l.append(l2)			# append another list object at end of list

l.remove([20, 30])		# remove the first occurrence of specified item
lastItem = l.pop()		# remove last item and store in variable
itm = l.pop(2)			# remove item at specified index and store in variable

l.reverse()				# reverse list in place
l.sort()				# sort list in place
l3 = sorted(l, reverse=True) # copy of sorted list

minval = min(l)			# minimum value in list
naxval = max(l)			# maximum value in list
sumvals = sum(l)		# sum of all values in list
itm = 20
idx = l.index(itm)		# get specific item index
check = (23 in l)		# check if a value exists in list


# for i, item in enumerate(l):		# for-loop enumerated list
# 	print(f'index: {i}, value: {item}')

def lst_to_str(l, sep=' - '):
	# convert list to string, using separator
	return sep.join([str(i) for i in l])

# ls = lst_to_str(l)
# print(ls)

def str_to_lst(s, sep=' - '):
	# convert string to list, using separator
	return s.split(sep)

# l = str_to_lst(ls)
# print(l)



# ------------------------------------------------------------------------------
#
# ------------------------------- Tuples ---------------------------------------

# tuples use parentheses
# they are immutable (cannot be modified) but are lighter
# so use for lists that will not change

# new tuple object
tup = ()
tup = tuple()



# ------------------------------------------------------------------------------
#
# ---------------------------- Dictionaries ------------------------------------

# dictionaries store key/value pairs

# new dict object
dct = {}
dct = {'name': 'Mick', 'age': 25, 'interests': ['travel', 'sport']}

s = dct['name']			# get value of 'name' key
lst = dct['interests']	# get value of 'interests' key
check = ('job' in dct)  # check if 'job' key exists
s = dct.get('job', 'key not found') 	# get 'job' value or default
dct['job'] = 'Janitor'
s = dct.get('job', 'key not found')

# add new key-value pairs and/or modify existing
dct.update({'name': 'Maurice', 'age': 27, 'hobbies': ['dance', 'paint']})

del dct['name']			# remove specified entry
s = dct.pop('job')		# remove specified entry and store in variable

dct_len = len(dct)			# numer of entries (dict length)
# print(dct.keys())
# print(dct.values())
# print(dct.items())

# for key, value in dct.items():
# 	print(key, value)

dct.clear()				# remove all entries
