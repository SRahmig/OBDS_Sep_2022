#for i in range (-1, -11, -1):
    #print(i)



number = int(input('Enter an integer : '))
total=0
for i in range (1,number+1):
    total=total+i
print(total)

#all prime numbers between 1 and 50
for i in range (1, 50):
    for j in range (2,i):
        if (i % j) ==0:
            break
    else:
        print(i)

#option 2 for prime numbers
for i in range (1, 50):
    is_prime=True
    if i > 1:
        for j in range (2,i):
            if (i % j) ==0:
                is_prime=False
    if is_prime == True:
        print(i)