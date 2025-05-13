arr = list(map(str, input("")))

long = 0
counter = 0
 
for num in range(len(arr)): # AGGGCT
    current = arr[num]
    
    if len(arr) == 1:
        long = 1
        
    elif num == 0 and current != arr[num+1]: # IF FIRST ONE
        counter += 1

        if counter > long:
            long = counter
            counter = 0
        else: 
            counter = 0
            pass

    elif num == (len(arr) - 1): # IF END
        counter += 1

        if counter > long:
            long = counter
            counter = 0
        else: 
            counter = 0
            pass

    elif current ==  arr[num+1]: # IF NEXT STILL CONTINUE
        while current ==  arr[num+1]:
            counter += 1
            break
    elif current != arr[num+1]: # IF NEXT STOPS
        counter += 1

        if counter > long:
            long = counter
            counter = 0
        else: 
            counter = 0
            pass

print(long)