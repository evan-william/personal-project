class system():
    def __init__(self):
        self.Length = 0

    def readInput(self):
        Length = int(input(""))
        if Length < 6   or Length >= 2000000000:
            print("0")
        else:
            self.compute(Length)

    def compute(self, Length):
        ArrayLong = []

        FinalLength = Length // 2
        Long1 = FinalLength - (FinalLength - 1)  # = 1
        Long2 = FinalLength - Long1              # = FinalLength - 1
        for _ in range(2):
            ArrayLong.append(Long1)
        for _ in range(2):
            ArrayLong.append(Long2)

        while Long1 != Long2:
            Long1 += 1
            Long2 -= 1
            if Long1 != Long2 and Long1 not in ArrayLong and Long2 not in ArrayLong:
                for _ in range(2):
                    ArrayLong.append(Long1)
                for _ in range(2):
                    ArrayLong.append(Long2)
            else:
                break

        TotalWays = len(ArrayLong)
        FinalWays = TotalWays // 4
        print(FinalWays)

def main():
    System = system()
    System.readInput()

if __name__ == "__main__":
    main()
