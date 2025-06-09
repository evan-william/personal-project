# Finished (Codeforces Rating >= 2200 (Extra), Difficulty: 2)
def main():
    TableInformation = input("") # 6,12
    RowCol, Target = TableInformation.split(" ")
    TableGenerator(RowCol, Target)

def TableGenerator(RowCol, Target):
    Table = []
    RowCol = int(RowCol)

    for Num in range(1, RowCol + 1): 
        for Num2 in range(1, RowCol + 1): 
            Number = Num * Num2
            Table.append(Number)
    TargetChecker(Table, Target)

def TargetChecker(Table, Target):
    TargetFound = 0
    for each in Table:
        if each == int(Target):
            TargetFound += 1
        
    print(TargetFound)

main()