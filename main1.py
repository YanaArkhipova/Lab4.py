n=int(input("Число від 1 до 9: "))
p= ["  _~_    ",
    " (o o)   ", 
    " / V \\   ",
    "/( s )\\  ",
    " ^^ ^^   "]
for line in p:
    for i in range(1,n+1):
        print(line.replace("s", str(i)), end=' ')
    print()
