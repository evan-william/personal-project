def main():
    Year = input("")
    print(f"{detector(Year)}") # Contoh: 1987
    
def detector(Year):
    tempo = []
    result = ""
    Year = int(Year) + 1
    Year = str(Year)
    LEBAR = len(Year)
    
    while len(tempo) < LEBAR:
        for num in str(Year): 
            if num not in tempo:
                tempo.append(num)
            elif num in tempo:
                tempo = []
                Year = int(Year) + 1
                break
                
    for numby in tempo:
        result += numby
    return int(result)
           
main()
        
        
        
        
        
        
        
    
    
    