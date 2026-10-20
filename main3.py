a=input("Enter the sring: ")
b=input("Enter the symbol: ")
c=a.find(b)
d=a.rfind(b)
if b in a:
    if c==d:
        print(c)
    else: 
        print(c, d)
else:
    print("missing")
