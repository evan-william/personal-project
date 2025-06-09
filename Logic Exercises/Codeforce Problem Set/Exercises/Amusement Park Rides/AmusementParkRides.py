# Not Finished Yet (European Championship 2025 - Online Mirror (Unrated, ICPC Rules, Teams Preferred))
def main():
    TestCase = input("")
    attraction(TestCase)

def attraction(TC): 
    for _ in range(int(TC)): # 3
        AttractionTime = []
        NumberOfAttraction = input("")
        VariousTime = input("")
        # VariousTime = list(map(int, input().split()))

        for each in VariousTime:
            if each == " ":
                pass
            else:
                AttractionTime.append(each)

        Current_Time = 0
        AttractionTime = sorted(AttractionTime)
        for each in AttractionTime: # [1,1,2,2,2,2]
            each = int(each)
            if Current_Time < each:
                Current_Time = each
            else:
                Current_Time += 1

        
        print(Current_Time)


main()