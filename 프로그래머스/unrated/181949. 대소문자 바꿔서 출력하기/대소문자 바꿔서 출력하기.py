str = input()
string = ''
for i in str:
    if i.isupper() == True:
        i = i.lower()
    else:
        i = i.upper()
    string += i
print(string)