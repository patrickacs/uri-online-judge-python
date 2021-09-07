TM = input().split()
A = int(TM[0])
B = int(TM[1])
C = int(TM[2])

if A == B or A == C or B ==C:
    print('S')

elif A == ( B + C) or B == (A + C) or C == (A + B):
    print('S')

elif A == ( B - C) or B == (A - C) or C == (A - B):
    print('S')

else:
    print('N')