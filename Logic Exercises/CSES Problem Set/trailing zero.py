num = int(input(""))
fak = 1

for _ in range(1,num+1):
    fak = fak * _
    
counter = 0
total = 0

total_fak = []
for each in str(fak):
    total_fak.append(each)

for current in range(len(total_fak)):
    try:
        if total_fak[current] and total_fak[current + 1] == "0":
            counter += 1
            total = counter
        elif total_fak[current] == "0" and total_fak[current + 1] != "0":
            counter += 1
            total = counter
    except IndexError:
        if total_fak[-1] == "0":
            counter += 1
            total = counter
        else:
            pass

    if total_fak[current] != "0":
        counter = 0

print(total)
    
    
    

