# Not Finished Yet (Codeforces Rating >= 2200 (Extra), Difficulty: 2)
def main():
    WordsInLecture, WordsEachLanguage = input("").split()
    lecturecheck(WordsInLecture, WordsEachLanguage)

def lecturecheck(WIL, WEL): # 4 3
    Translation = []
    FirstLanguage = []
    SecondLanguage = []
    State = 0 # Index Checking
 
    # Stores Dictionary
    for _ in range (WEL):
        FirstLanguageInput, SecondLanguageInput = input("").split() # codeforces codesecrof
        FirstLanguage.append(FirstLanguageInput) # codeforces 
        SecondLanguage.append(SecondLanguageInput) # codesecrof

    # Lecture Input
    Word = list(map(str, input().split())) # [codeforces, contest, letter, contest] 

    for every in Word[State]: # Checks both language (4)
        if every in FirstLanguage or SecondLanguage: # Detects if it exist
            ...

            

main()