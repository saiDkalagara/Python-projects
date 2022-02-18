a=4
b=5

c = a > b # False
d = a < b # True

e = a == b # False
f = a != b # True

g = not e # True

h = e and f # False  ## Its false because False and True = False
j = e or f # True   ## Its True because False or True = True

if e:
    print('e is true')
elif g:
    print('this one always will print')
else:
    print('e lied')

