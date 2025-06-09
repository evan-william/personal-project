t = int(input(""))

Line1 = [1,2,9,10,15]
Line2 = [4,3,8,11,24]
Line3 = [5,6,7,12,23]
Line4 = [16,15,14,13,22]
Line5 = [17,18,19,20,21]

for _ in range(t): # Run Each Test Case
    y , x = input("").split(" ")

    y = int(y)
    x = int(x)

    if y == 1:
        print(Line1[x - 1])
    elif y == 2:
        print(Line2[x - 1])
    elif y == 3:
        print(Line3[x - 1])
    elif y == 4:
        print(Line4[x - 1])
    elif y == 5:
        print(Line5[x - 1])

