class System():
    def __init__(self):
        self.array = []
        self.firsthalf = []
        self.secondhalf = []
        self.correctarray = []

    def readinput(self):
        self.input = list(map(int, input(""))) # AAAACACBA
        self.reorder(self.input)
        
    def reorder(self, input):
        for each in input:
            self.length = len(each)
            self.firsthalflength = self.length / 2
            for _ in range(self.firsthalflength):
                ...

def main():
    system = System()
    system.readinput()
    
if __name__ == "__main__":
    main()

        