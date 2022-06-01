'''
LEGB
Local, Enclosing, Global, Built-in
'''

import builtins
print(dir(builtins))

print('-'*15)

x = 'global x'
y = 'global y'
z = 'global z'


def func():
    # func local scope
    # also, subfunc enclosing scope
    x = 'func local x'
    global y
    y = 'func y'
    z = 'func local z'

    def subfunc():
        # subfunc local scope
        x = 'subfunc local x'
        nonlocal z
        z = 'subfunc local z'
        print(x)
        print(z)

    subfunc()
    print(x)
    print(y)
    print(z)


print(x)
print(y)
print(z)
func()
print(x)
print(y)
print(z)
