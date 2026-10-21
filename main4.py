n=input("Введіть вираз: ")
a=0
for i in n:
    if i=="(":
        a+=1
    elif i==")":
        a-=1
    elif a<0:
        break
print(a==0)
