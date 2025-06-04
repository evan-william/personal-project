# Finished (Codeforces Rating >= 2200 (Extra), Difficulty: 1)
def main():
    WrittenNumber = input("")
    WrittenA, WrittenB = WrittenNumber.split(" ")
    WinChecker(int(WrittenA),int(WrittenB))

def NeutralChecker(WA, WB, S):
    if WA - S  >= 0:
        WA = WA - S
    elif WA - S < 0:
        WA = S - WA

    if WB - S >= 0:
        WB = WB - S
    elif WB - S < 0:
        WB = S - WB
    
    return WA, WB

def WinChecker(WrittenA, WrittenB):
    Way1Win = 0 # 1st Player Win
    WayNoWin = 0 # Draw
    Way2Win = 0 # 2nd Player Win
    Dice = [1,2,3,4,5,6]

    for State in Dice:
         WrittenAB = NeutralChecker(WrittenA, WrittenB, State)
         WinWrittenA = WrittenAB[0]
         WinWrittenB = WrittenAB[1]
            
         if WinWrittenA < WinWrittenB: # 2,5 
            Way1Win += 1
         elif WinWrittenA > WinWrittenB:
            Way2Win += 1
         else:
            WayNoWin += 1
    
    print(f"{Way1Win} {WayNoWin} {Way2Win}")
    
main()

