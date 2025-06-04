"""
def main():
    ternary = input("Please input the code: ").strip()
    result = ""
    char = 0

    while char < len(ternary):
        if ternary[char] == ".":
            result += "0"
            char += 1
        elif ternary[char] == "-":
            if ternary[char + 1] == ".":
                result += "1"
            elif ternary[char + 1] == "-":
                result += "2"
            char += 2  
        else:
            raise ValueError("Invalid EvanError")

    print(result)

main()
"""

def main():
    ternary = input().strip()
    result = ""
    char = 0

    while char < len(ternary):
        if ternary[char] == ".":
            result += "0"
            char += 1
        elif ternary[char] == "-":
            if ternary[char + 1] == ".":
                result += "1"
            elif ternary[char + 1] == "-":
                result += "2"
            char += 2 

    print(result)

main()

