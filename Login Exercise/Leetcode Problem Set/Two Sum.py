# Two Sum (Easy)
class Solution():
    def __init__(self):
        self.nums = []
        self.target = ""
        self.index = []  # pindahin ke sini biar gak ke-reset tiap loop1

    def twoSum(self, nums, target):
        for loop1 in range(len(nums)):
            INDEXFINDER = loop1  # langsung pakai loop1 aja, jangan nums.index()

            for loop2 in range(loop1 + 1, len(nums)):
                check = nums[loop1] + nums[loop2]
                if check == target:
                    INDEXFINDER2 = loop2  # langsung pakai loop2 juga

                    # kalau pasangan belum ada di self.index
                    if [INDEXFINDER, INDEXFINDER2] not in self.index:
                        self.index.append([INDEXFINDER, INDEXFINDER2])
                    else:
                        pass
                else:
                    pass
        
        # Tampilkan hasilnya
        for pair in self.index:
            print(pair)

    def readinput(self):
        self.first = input("nums = ")
        for each in self.first:
            if each.isnumeric():
                self.nums.append(each)
            else:
                pass
        # self.nums = list(map(int, input("nums = ").split(","))) # input: 5,1,2,3,7,1,7,2,8,2,10,4
        self.target = int(input("target = "))                   # input: 14
        self.twoSum(self.nums, self.target)

def main():
    solution = Solution()
    solution.readinput()

if __name__ == "__main__":
    main()
