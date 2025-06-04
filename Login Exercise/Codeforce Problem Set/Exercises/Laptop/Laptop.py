def main():
    Amount = int(input(""))
    laptopinfo(Amount)
    
def laptopinfo(A):
    Price = []
    Quality = []
    
    while(A != 0):
        A -= 1
        PriceQuality = input("")
        Prices, Qualitys = PriceQuality.split(" ")
        
        Price.append(int(Prices))  # Convert to integer
        Quality.append(int(Qualitys))  # Convert to integer
        
    combineinfo = zip(Price, Quality)
    Price, Quality = zip(*combineinfo)
    checker(Price, Quality)

def checker(Price, Quality):
    ConditionCheck1 = 0 # Low Price High Quality
    ConditionCheck2 = 0 # High Price Low Quality
    StateCheck = 0 # Which Laptop to Compare
    
    for _ in Price:  
        if int(Price[StateCheck]) > int(Quality[StateCheck]):  # Ensure integer comparison
            ConditionCheck1 = 1
            
        elif int(Price[StateCheck]) < int(Quality[StateCheck]):
            ConditionCheck2 = 1
            
        StateCheck += 1  # Move index after checking conditions
    
    if ConditionCheck1 == 1 and ConditionCheck2 == 1:
        print("Happy Alex")
    else:
        print("Poor Alex")
        
main()
