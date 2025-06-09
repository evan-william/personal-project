# Not Finished (Codeforces Rating >= 2200 (Extra), Difficulty: 1)
def main():
    OpponentsInfo = input("") # 2 2
    beatcheck(OpponentsInfo)

def beatcheck(OInfo):
    NumberOfOpponents, NumberOfDays = OInfo.split(" ")
    Streak = 0 # Beating in a row
    
    for _ in range(int(NumberOfDays)): # Which Day
            CurrentDay = []
            Absent = input("")

            CurrentDay.append(Absent)
            if 0 in CurrentDay:
                Streak = 0
            else:
                Streak += 1

    print(Streak)
                


            



main()