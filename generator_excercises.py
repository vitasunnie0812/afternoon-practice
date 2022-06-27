#Generator Excercises

#Problem 1
#Create a generator, primes_gen that generates prime numbers starting from 2.

def primes_gen():
    n=2
    while True:
        count=0
        for i in range(2,n):
            # if n is divisible by any number btw 2 and itself-1 then increase count by 1
            if n % i == 0:
                count+=1
        # if count is =0 then the number is only divisible by 1 and itself
        if count == 0 :
            yield n
        n+=1

gen = primes_gen()
for _ in range(10):
    print(next(gen), end=' ')
# Expected output
# 2 3 5 7 11 13 17 19 23 29
#----------------------------------------------------------------------------

print('\n')


#Problem 2
#Create a generator, unique_letters that generates unique letters from
#the input string. It should generate the letters in the same order as
#from the input string.

def unique_letters(str0):
    i=0
    while i <= len(str0)-1:
        yield str0[i]
        i+=1

for letter in unique_letters('hello'):
    print(letter, end=' ')
# Expected output
# h e l o