x = 10 # Global

def my_function():
    global x,y
    x = 4
    y = 5 # Local Variable
    
    print(y)

my_function()
print(x)
print(y)