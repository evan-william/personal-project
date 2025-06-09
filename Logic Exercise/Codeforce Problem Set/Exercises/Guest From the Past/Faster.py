class System:
    def compute(self, R, PB, GB, EB):
        # Kalau plastik lebih murah, langsung beli sebanyak-banyaknya
        if PB <= GB - EB:
            print(R // PB)
            return
        
        # Kalau beli botol kaca bisa dikembalikan, kita lakukan strategi recycle
        max_drinks = 0
        
        # Beli pertama kali sebanyak mungkin botol kaca
        initial_bottles = R // GB
        R %= GB
        
        total_drinks = initial_bottles
        empty_bottles = initial_bottles
        
        # Tukar botol kosong selama cukup uang
        while empty_bottles > 0:
            # Kembalikan semua botol kosong, dapatkan refund
            R += empty_bottles * EB
            bottles_bought = R // GB
            R %= GB
            
            if bottles_bought == 0:
                break
            
            total_drinks += bottles_bought
            empty_bottles = bottles_bought

        print(total_drinks)

    def readinput(self):
        R = int(input())      # Rubel
        PB = int(input())     # Harga botol plastik
        GB = int(input())     # Harga botol kaca
        EB = int(input())     # Uang kembali dari botol kaca
        self.compute(R, PB, GB, EB)

def main():
    system = System()
    system.readinput()

if __name__ == "__main__":
    main()
