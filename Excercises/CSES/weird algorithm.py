n = int(input())

ways = []
ways.append(n)

while n != 1:
    if n % 2 == 0: # Even
        n = n // 2
        ways.append(n)
    elif n % 2 == 1: # Odd
        n = (n * 3) + 1
        ways.append(n)
    
print(*ways)