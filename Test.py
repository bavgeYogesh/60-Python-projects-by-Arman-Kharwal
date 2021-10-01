
text = str(input("enter the text"))
splitted_text = text.split()
for i in splitted_text:
    print(i[0].upper(),end="")

print()
a=""
for i in splitted_text:
    a = (a + i[0]).upper()
print(a)