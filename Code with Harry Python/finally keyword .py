# try:
#     l = [1,5,6,7]
#     i = int(input('Please Enter The Index" '))
#     print(l[i])
# except:
#     print('error')
    
# finally:
#     print('Always Executed')



def func1():
    try:
        l = [1,5,6,7]
        i = int(input('Please Enter The Index" '))
        print(l[i])
    except:
     print('error')
    
    finally:
        print('Always Executed')
        
        
x = func1()

print(x)