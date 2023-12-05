a = input("Normal English: ")
x = list(a)
while len(x) < 4:
    m = input('random: ')
    x.append(input(m))
    
    x.reverse()
    print(x)
    
