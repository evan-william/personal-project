def main():
    count = int(input(""))
    convert(count)
    
def convert(c):
    
    convertlist = []
    
    for _ in range(c):
        list = ""
        word = input("")
        list = list + word
        if len(list) > 10:
            first = list[0]
            last = list[-1]
            midcount = -2
            
            for i in list:
                midcount += 1
            convert = str(first) + str(midcount) + str(last)
            convertlist.append(convert)
        else:
            convertlist.append(list)
            
    for last in convertlist:
        print(last)
            

main()
        

    
