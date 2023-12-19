marks = [12,56,32,98,12,45,1,4]
# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print('I am Awesome')
#     index +=1
    
    # index first in order and then value
    
    
    
# for index,mark in enumerate(marks):
#     print(mark)
#     if (index == 3):
#         print('I am Awesome')

# index always start at 0 but u can change it 


for index,mark in enumerate(marks, start=1):
    print(mark)
    if (index == 3):
        print('I am Awesome')
