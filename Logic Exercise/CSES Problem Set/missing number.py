n = int(input())

num = list(range(1, n + 1))
ins_num = list(map(int, input().split(" ")))

missing = list(set(num) - set(ins_num)) # ARRAY DIFF

print(*missing)