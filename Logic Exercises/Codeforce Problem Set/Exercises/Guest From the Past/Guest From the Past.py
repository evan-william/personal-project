# Codeforces Rating >= 2200 (Extra), Difficulty: 4
class System():
    def __init__(self):
        self.rubles = 0
        self.plasticBottle = 0 # Cost a rubble (Unreturnable)
        self.glassBottle = 0 # Cost b rubble
        self.emptyBottle = 0 # Return to get c (c < b) rubles back
        self.TempoMaxDrink_A = 0 # Tempo Max A & B
        self.TempoMaxDrink_B = 0
        self.MaxDrink = 0 # Max Liter He Can Drink
        self.EmptyGlassBottle = 0
        self.Difference = 0 # If Buy Sell is Better than Buy Non Sellable
        
    def compute(self, R, PB, GB, EB):
        EmptyGlassBottle = self.EmptyGlassBottle
        Difference = self.Difference
        Difference = GB - EB

        # Check Which is Cheaper
        if PB > GB and Difference < PB: # Glass Bottle Lower    
            while ( R >= 0 ): 
                R -= GB
                if R >= 0:
                    self.MaxDrink += 1
                    EmptyGlassBottle += 1 # Drinked and Can be Returned
                    if EmptyGlassBottle > 0: # Check if have empty Bottle
                        EmptyGlassBottle -= 1
                        R += EB # Returned the Bottle
                    else: 
                        pass # Pass if no empty Bottle
                else:
                    pass
        elif GB > PB: # Plastic Bottle Lower
            while ( R >= 0 ):
                R -= PB
                if R >= 0:
                    self.MaxDrink += 1
                else:
                    pass
        elif GB == PB: # Use Default If Same
            while ( R >= 0 ): 
                R -= GB
                if R >= 0:
                    self.MaxDrink += 1
                    EmptyGlassBottle += 1 # Drinked and Can be Returned
                    if EmptyGlassBottle > 0: # Check if have empty Bottle
                        EmptyGlassBottle -= 1
                        R += EB # Returned the Bottle
                    else: 
                        pass # Pass if no empty Bottle
                else:
                    pass
    
        # Show Best Output
        print(self.MaxDrink)
        
    def readinput(self):
        rubles = int(input(""))
        plasticBottle = int(input(""))
        glassBottle = int(input(""))
        emptyBottle = int(input(""))
        self.compute(rubles, plasticBottle, glassBottle, emptyBottle)
 
def main():
    system = System()
    system.readinput() 

if __name__ == "__main__":
    main()


    