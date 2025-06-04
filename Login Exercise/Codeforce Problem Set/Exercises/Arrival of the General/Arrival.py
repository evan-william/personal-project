def main():
    soldier = input("")
    soldierHeight = list(map(int, input("").split(" "))) # ['11','22','33','44']
    heightCheck(soldierHeight)
    
def heightCheck(H):
    maxHeight = max(H)
    minHeight = min(H)
    switcher(maxHeight,minHeight,H)
    
def linear_Maxsearch(H, max):
    for i in range(len(H)):
        if H[i] == max:
            return i
        
def linear_Minsearch(H, min):
    for i in range(len(H) - 1, -1, -1):
        if H[i] == min:
            return i
        
def switcher(max,min,H):
    tempo = 0
    x = linear_Maxsearch(H, max)
    while H[0] is not max and x > 0:
        H[x],H[x-1] = H[x-1],H[x]
        x -= 1
        tempo += 1
    
    y = linear_Minsearch(H, min)
    while H[-1] is not min and y < len(H) - 1:
        H[y],H[y+1] = H[y+1],H[y]
        y += 1
        tempo += 1 
    print(tempo)
    
main()