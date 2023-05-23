import random

n = int(input())
if n < 15 or n > 35:
    raise Exception("Invalid number")

lis1 = []

#lis1 = [random.randint(30, 300) for _ in range(n)]
#print(lis1)

for i in range(n):
    i = int(input())
    if i < 30 or i > 300:
        raise Exception("Wrong number")
    else:
        lis1.append(i)
print(lis1)

count = 0
for i in lis1:
    if (i // 10) % 10 == 3 or (i // 10) % 10 == 6 or (i // 10) % 10 == 9:
        count += 1
print(count)

min_number = min([x for x in lis1 if x % 6 == 4])
print(lis1.index(min_number))

#for x in lis1:
    #if x >= 10 and x < 100 and (x % 3 == 0 or x % 2 == 0):
        #print(x)
        
lis2=[x for x in lis1 if 10 <= x < 100 and (x % 3 == 0 or x % 2 == 0)]  
print(lis2)  

sum = 0 
for n in lis2[1::2]:
    sum += n

avarage  = sum / len(lis2[1::2])
print(avarage)

even_number = min([x for x in lis2 if x % 2 == 0])
#min_even = min(even_numbers)
print(even_number)
lis2.remove(even_number)
#lis2 = [x for x in lis2 if x != even_number]
print(lis2)


