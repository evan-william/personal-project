k = int(input())

for num in range(1,k+1):
    numf = pow(num,2)

    initial_pos = numf * (numf - 1) // 2

    bad_pos = 4 * (num - 1) * (num - 2)

    correct_pos = initial_pos - bad_pos
    print(correct_pos)

    

