a=int(input("Enter the number (0 < m ≤ 255): "))
b=input("Enter the text: ")
words=b.split()
line=" "

for word in words:
    if line==" ":
        line=word
    elif len(line)+1+len(word)<=a:
        line=line+" "+word
    else:
        print(line)
        line=word
print(line)
