def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print(" Thanks for Using This Function")
    return mfx

@greet

def hello():
    print("Hello World")
    
def add (a,b):
    print(a+b)
    
hello()

# greet(hello)()