# def average(a=9, b = 1):
#     print("The Avergage is ", (a+b)/2)
    


# average(b=9 , a=21)




# def name(fname , mname ="john", lname ="Whatson"):
#     print("Hello,",fname , mname , lname)
# name("amy","Agarwal","jain")


def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    
    # print("Average is: ",sum/len(numbers))
    return sum /len(numbers)
    return 7



c = average(5,6,7,1)
print(c)
    
# average(5,1,8)