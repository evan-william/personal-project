# Finished (Codeforces Rating >= 2200 (Extra), Difficulty: 2)
def main():
    TableInformation = input("") # 6,12
    RowCol, Target = TableInformation.split(" ")
    TableGenerator(RowCol, Target)

def TableGenerator(RowCol, Target):
    RowCol = int(RowCol)
    TargetFound = 0

    for Num in range(1, RowCol + 1): 
        for Num2 in range(1, RowCol + 1): 
            Number = Num * Num2
            if Number == int(Target):
                TargetFound += 1
            
    print(TargetFound)
    
main()