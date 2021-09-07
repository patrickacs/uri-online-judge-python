idades = input().split()
h = int(idades[0])
z = int(idades[1])
l = int(idades[2])
if z < h < l or l < h < z:
    print('huguinho')

elif l < z < h or h < z < l:
    print('zezinho')

else:
    print('luisinho')