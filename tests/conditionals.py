
# ------------------------------------------------------------------------------
#
# ------------------------ comparison operators --------------------------------

boo = (3 == 2)      # Equal:            ==
boo = (3 != 2)      # Not Equal:        !=
boo = (3 > 2)       # Greater Than:     >
boo = (3 < 2)       # Less Than:        <
boo = (3 >= 2)      # Greater or Equal: >=
boo = (3 <= 2)      # Less or Equal:    <=
a, b = 3, 2
boo = (a is b)      # Object Identity:  is


# ------------------------------------------------------------------------------
#
# ----------------------------- False values -----------------------------------

# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.


condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
