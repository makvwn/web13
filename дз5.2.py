string="this concludes my essay. put a five, Maria Ivanovna! i tried very hard!" 
new_string = ""
f = True
for i in string:
    if i == "." or i == "!":
        f = True
        new_string += i
    elif i.isalpha() and f:
        i = i.upper()
        f = False
        new_string += i
    else:
        new_string += i
print("before:\n", string, "\nafter:\n", new_string)