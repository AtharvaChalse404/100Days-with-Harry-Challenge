a= 330
b = 3303

print("a") if a > b else print("=") if a == b else print("B")


if a > b:
    if a == b:
        pass
    else:
        print("B")
    print("a")
else:
    print("=")