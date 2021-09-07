from math import floor

b = float(input())
g = float(input())

if g % 2 != 0:
    g = floor(g / 2)
else:
    g /= 2
precisa = g - b

if precisa > 0:
    print('Faltam {} bolinha(s)'.format(str(round(precisa))))

else:
    print('Amelia tem todas bolinhas!')
