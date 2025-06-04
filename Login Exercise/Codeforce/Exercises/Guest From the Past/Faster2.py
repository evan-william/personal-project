class System:
    def compute(self, R, a, b, c):
        if a <= b - c:
            print(R // a)
        else:
            if R < b:
                print(0)
            else:
                print(1 + (R - b) // (b - c))

    def readinput(self):
        R = int(input())
        a = int(input())
        b = int(input())
        c = int(input())
        self.compute(R, a, b, c)

def main():
    system = System()
    system.readinput()

if __name__ == "__main__":
    main()
