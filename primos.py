import math
number = int(input())
prime_number = []
for i in range(2, number + 1):
    prime_number.append(i)
i = 2
while i <= int(math.sqrt(number)):
    if i in prime_number:
        for j in range(i * 2, number + 1, i):
            if j in prime_number:
                prime_number.remove(j)
    i = i + 1
print (prime_number)