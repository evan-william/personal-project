# Finished (Codeforces Rating >= 2200 (Extra), Difficulty: 1)
def main():
    Information = input("") # 3 17 4
    count(Information)

def count(Info):
    FirstBananaCost, HowMuchHave, WantBanana = Info.split(" ")
    BananaCounter = 1
    TotalCost = 0
 
    for _ in range(int(WantBanana)):
        TotalCost += BananaCounter * int(FirstBananaCost)
        BananaCounter += 1
    
    Borrow = int(HowMuchHave) - TotalCost

    if Borrow <= 0:
        print(abs(Borrow)) # PRINT POSITIVE EVEN IF ITS NEGATIVE
    else:
        print("0")

main()