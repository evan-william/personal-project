# Finished (Codeforces Rating >= 2200 (Extra), Difficulty: 1)
def main():
    QueueInformation = input("") # 5 7
    distress(QueueInformation)

def distress(QI):
    GiveOrTakeQueue = [] # A supplier or a kid
    PacksQueue = [] # How many packs
    QueuePlusMin, FirstStatePack = QI.split(" ")
    DistressedKiddo = 0 
    MinusTempo = 0 # Temporary Variable

    for _ in range(int(QueuePlusMin)):
        PersonInfo = input("")
        GiveOrTake, HowMany = PersonInfo.split(" ")
        GiveOrTakeQueue.append(GiveOrTake)
        PacksQueue.append(HowMany)

    FirstStatePack = int(FirstStatePack)

    for Queue in PacksQueue: # 10 20 30
        Queue = int(Queue)
        for PlusOrMin in GiveOrTakeQueue: # + - + -
            if PlusOrMin == "+":
                FirstStatePack += Queue
                GiveOrTakeQueue.remove(PlusOrMin)
                break
            elif PlusOrMin == "-":
                MinusTempo = FirstStatePack 
                MinusTempo -= Queue
                if MinusTempo < 0:
                    DistressedKiddo += 1
                    GiveOrTakeQueue.remove(PlusOrMin)
                    break
                else:
                    FirstStatePack -= Queue
                    GiveOrTakeQueue.remove(PlusOrMin)
                    break

    print(FirstStatePack)
    print(DistressedKiddo)
                    
main()