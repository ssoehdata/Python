rawstr = input('enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('well done Dave')
else:
    print('not a number')
    