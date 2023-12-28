x = 4


def hello():
    x = 5
    print(f'The Local x is {x}')
    y = 1
    print('Hello')
    
hello()

print(f"The Global X Is {x}")

print(local.y)