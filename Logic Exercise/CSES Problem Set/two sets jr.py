num = int(input())

arr_num = []
arr_num_A = []
arr_num_B = []

for _ in range(1, num+1):
    arr_num.append(_)

total = sum(arr_num)
target = total // 2

if total % 2 == 1:
    print("NO")

elif total == 6:
    print("YES")
    print(1)
    print(3)
    print(2)
    print("1 2")

else:
    INITIAL_STATE_1 = 0
    INITIAL_STATE_2 = len(arr_num) - 1

    current_sum = 0  # <== Track manually, faster!

    while current_sum != target:
        arr_num_A.append(arr_num[INITIAL_STATE_1])
        current_sum += arr_num[INITIAL_STATE_1]
        if current_sum == target:
            break

        arr_num_A.append(arr_num[INITIAL_STATE_2])
        current_sum += arr_num[INITIAL_STATE_2]
        if current_sum == target:
            break

        last_piece_finder = target - current_sum

        if 1 <= last_piece_finder <= num and last_piece_finder not in arr_num_A:
            arr_num_A.append(last_piece_finder)
            current_sum += last_piece_finder
            break
        else:
            INITIAL_STATE_1 += 1
            INITIAL_STATE_2 -= 1

    arr_num_set = set(arr_num)
    arr_num_A_set = set(arr_num_A)

    arr_num_B = arr_num_set - arr_num_A_set

    print("YES")
    print(len(arr_num_A_set))
    print(*arr_num_A_set)
    print(len(arr_num_B))
    print(*arr_num_B)
