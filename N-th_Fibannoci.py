def fibanocci(n,dict={}):
    key = n
    if(n in dict):
        return dict[key]
    if(n<=2):
        return 1
    dict[key] = fibanocci(n - 1,dict) + fibanocci(n - 2,dict)
    return dict[key]

print(fibanocci(10))
print(fibanocci(50))
print(fibanocci(3))
print(fibanocci(2))
