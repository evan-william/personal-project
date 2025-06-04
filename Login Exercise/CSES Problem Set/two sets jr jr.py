num = int(input(""))

arr_num = []
arr_num_A = []
arr_num_B = []

for _ in range(1,num+1):
    arr_num.append(_) # [1,2,3,4,5,6,7]

total = sum(arr_num) # 28
target = total // 2 # 14 14 

if total % 2 == 1: 
        print("NO")

elif total == 6:
    print("YES")

    print("1") 
    print("3")

    print("2")
    print("1 2")

else:   
    INITIAL_STATE_1 = 0 # START
    INITIAL_STATE_2 = len(arr_num) - 1 # END

    current_sum_A = 0

    while current_sum_A != target:
        arr_num_A.append(arr_num[INITIAL_STATE_1])
        current_sum_A += arr_num[INITIAL_STATE_1]
        if current_sum_A == target:
             break

        arr_num_A.append(arr_num[INITIAL_STATE_2])
        current_sum_A += arr_num[INITIAL_STATE_2]
        if current_sum_A == target:
             break

        last_piece_finder = target - current_sum_A

        if 1 <= last_piece_finder <= num and last_piece_finder not in arr_num_A:
             arr_num_A.append(last_piece_finder)
             current_sum_A += last_piece_finder
             break
        else:
             INITIAL_STATE_1 += 1
             INITIAL_STATE_2 -= 1

    arr_num = set(arr_num) # SPEED BOOST
    arr_num_A = set(arr_num_A) # SPEED BOOST
    
    arr_num_B = arr_num - arr_num_A

    print("YES")

    print(len(arr_num_A)) 
    print(*arr_num_A)

    print(len(arr_num_B))
    print(*arr_num_B)

        