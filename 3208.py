while True:
    k,l = input().split(" ")
    k = int(k)
    l = int(l)
    y = 0
    ver = False
    if k == 0 and l == 0:
        break
    else:
        for i in range(2, l):
            if(k % i == 0):
                ver = True
                y = i
                break
        if ver:
            print(f"BAD {y}")
        else:
            print("GOOD")