class System():
    def __init__(self):
        self.ArrayOfficial = []
        self.Distinct = 0

    def DistinctCheck(self, Data):
       ArrayOfficial = self.ArrayOfficial
       for each in Data:
           if each not in ArrayOfficial:
               ArrayOfficial.append(each)
           else:
               pass
       Distinct = self.Distinct
       Distinct = len(ArrayOfficial)
       print(Distinct)
               
    def ReadInput(self):
        self.Numbers = int(input(""))
        self.Data = list(map(int, input("").split(" "))) # 2 3 2 2 3
 
        if self.Numbers == len(self.Data):
            Data = self.Data 
            self.DistinctCheck(Data)
        else:
            print("Error!")
            
def main():
    system = System()
    system.ReadInput()


if __name__ == "__main__":
    main()