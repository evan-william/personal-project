def avg():
    Sum = 0
    Numbers = list(map(int, input("").split(" ")))
    for each in Numbers:
        Sum += each 
    Total = Sum / 2
    print(f"{Total:.2f}")

if __name__ == "__main__":
    avg()