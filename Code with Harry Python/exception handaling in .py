a = input("Enter Numbers: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}"  )
except Exception as e:
    print(e)
    
    
print("some imp line of code")