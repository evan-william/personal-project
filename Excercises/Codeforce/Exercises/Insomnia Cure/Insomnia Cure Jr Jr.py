def compute_damaged_dragons(k, l, m, n, d):
    if k == 1 or l == 1 or m == 1 or n == 1:
        # Semua dragon kena kalau salah satu kelipatannya 1
        print(d)
        return

    damaged = [False] * (d + 1)  # Index 0 tidak digunakan
    
    for x in (k, l, m, n):
        for i in range(x, d + 1, x):
            damaged[i] = True

    print(sum(damaged))  # Menghitung jumlah True

# Input
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

compute_damaged_dragons(k, l, m, n, d)
