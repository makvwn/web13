print ('a = ', end = '') 
 
a = int (input ()) 
 
print ('b = ', end = '') 
 
b = int (input ()) 
 
p = a * b 
 
while a != 0 and b != 0: 
 
    if a > b: 
 
        a = a % b 
 
    else: 
 
        b = b % a 
 
nod = a + b 
 
nok = p // nod 
 
print ('НОК введённых чисел:', nok)