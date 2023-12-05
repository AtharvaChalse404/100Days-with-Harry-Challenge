f0 = 0
f1 = 1

k = 15

series = []





for s in range(2,k):
    l = f0 + f1 
    series.append(l)
    f0, f1 = f1, f0 + f1
    
    
print(series)