for i in range(int(input())):
    x = input()
    if x != "P=NP":
        a, b = x.split("+")
        print(str(int(a) + int(b)))
    else:
        print("skipped")