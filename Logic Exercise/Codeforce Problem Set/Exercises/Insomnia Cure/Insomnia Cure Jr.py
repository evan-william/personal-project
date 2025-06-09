# Codeforces Rating >= 2200 , Difficulty 1
class system():
    def __init__(self):
        punched = self.Punched
        tailShut = self.TailShut
        pawsTrampled = self.PawsTrampled
        callMom = self.CallMom
        totalDragons = self.totalDragons

    def compute(punch, tail, paws, call, total):
        damagedDragons = 0

        if punch == 1:
            print(total)
        else:
            Dragon = []
            for _ in range(1,total+1):
                Dragon.append(_)
            
            minValue1 = punch
            minValue2 = tail
            minValue3 = paws
            minValue4 = call

            while punch <= total:
                try:
                    Dragon.remove(punch)
                    punch += minValue1
                    damagedDragons += 1
                except ValueError:
                    punch += minValue1
                    pass
            while tail <= total:
                try:
                    Dragon.remove(tail)
                    tail += minValue2
                    damagedDragons += 1
                except ValueError:
                    tail += minValue2
                    pass
            while paws <= total:
                try:
                    Dragon.remove(paws)
                    paws += minValue3
                    damagedDragons += 1
                except ValueError:
                    paws += minValue3
                    pass
            while call <= total:
                try:
                    Dragon.remove(call)
                    call += minValue4
                    damagedDragons += 1
                except ValueError:
                    call += minValue4
                    pass
                
            print(damagedDragons)
            
    def readInput():
        punched = int(input(""))
        tailShut = int(input(""))
        pawsTrampled = int(input(""))
        callMom = int(input(""))
        totalDragons = int(input(""))

        system.compute(punched, tailShut, pawsTrampled, callMom, totalDragons)
    
def main():
    system.readInput()

if __name__ == "__main__":
    main()