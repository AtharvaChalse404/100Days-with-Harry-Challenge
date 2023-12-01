x = int(input("please enter: "))


match x:
    case 0:
        print("zero")
    case 4:
        print("four")
    case 8:
        print("eight")    
        
        #this Means Default Value Smjla ka 
        # Hi Fakt Tevha Run Hoil Jevha Baki Saglya Case Statements Match Nahi Honar Jar Match Zhalya tar Tyacha Code Block Print Hoil
        # Match nahi zhali case Tar Defualt  Wala Run Hoil
    case _x:
        print(x)