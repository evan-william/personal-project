# DICE COMBINATIONS
Total = 0
Ways = 0

def system(wanted):
    global Total
    global Ways
    for each in range(1,7):
        for each2 in range(1,7):
            if Total != wanted:
                Total += each 
                while Total != wanted:
                    Total += each2
                Ways += 1
            else:
                Ways += 1
                break
    print(Ways)
                    
def main():
    wanted = input()
    system(wanted)
    
if __name__ == "__main__":
    main()