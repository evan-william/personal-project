n = int(input())
arr = list(map(int, input().split(" "))) # [3,2,5,1,7]

total = 0

for num in range(len(arr)):
    if arr[num] < arr[num-1]  and num != 0:
        x = arr[num]
        y = arr[num-1]

        distinct = x - y
        
        x += abs(distinct)
        arr[num] = x

        total += abs(distinct)   
    elif num == 0:
        pass
    else:
        pass

print(total)