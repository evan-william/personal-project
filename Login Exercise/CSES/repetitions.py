arr = list(map(str, input("")))

A_COUNT = arr.count("A")
C_COUNT = arr.count("C")
G_COUNT = arr.count("G")
T_COUNT = arr.count("T")

tot_arr = [A_COUNT, C_COUNT, G_COUNT, T_COUNT]
find_max = max(tot_arr)
print(find_max)
