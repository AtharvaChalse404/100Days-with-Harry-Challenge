a = int(input("Enter Any Value Between 5 and 9: "))

if (a< 5 or a > 9):
    raise ValueError("Value Should be Between 5 and 9")


# Quick Quiz

f = input('Please Enter QUIT')

try:
    if (f != 'QUIT'):
        raise ValueError
    else:
        print('You Have Entered QUIT NIce')
finally:
    True

