def main():
    GlobalInformation = input("")
    KiritoStrength, NumberOfDragons = GlobalInformation.split(" ")
    game(KiritoStrength, int(NumberOfDragons))
    
 
def game(KS, NoD):
    DragonStrengthArray = []
    BonusArray = []
    
    for Unit in range(NoD):
        DragonInformation = input("")
        DragonStrength, Bonus = DragonInformation.split(" ")
        DragonStrengthArray.append(int(DragonStrength))  
        BonusArray.append(int(Bonus))  
        
    wincondition(int(KS), NoD, DragonStrengthArray, BonusArray)  
        
def wincondition(KS, NoD, DSA, BA):
    stage = 0
    
    combined = sorted(zip(DSA, BA))  
    DSA, BA = zip(*combined)  
    
    for Fight in range(NoD):  # NoD Number of Dragons
        if KS > DSA[stage]:  # Compare correctly using int values
            KS += BA[stage]
            stage += 1
            result = 1
        else:
            result = 0
            break  
    
    if result == 1:
        print("YES")
    else:
        print("NO")
            
main()
