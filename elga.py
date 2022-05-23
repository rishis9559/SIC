import random

def gcd(a, b):
	if (a == 0):
		return b;
	return gcd(b % a, a);

def prime_list():
    i = 0
    while i<len(primes_list):
        ele = primes_list[i]
        j = i+1
        while j<len(primes_list):
            if(primes_list[j]%ele==0):
                primes_list.pop(j)
                j-=1
            j+=1
        i+=1
        
def nBitRandom(n):
    return random.randrange(2**(n-1)+1, 2**n - 1)


def getnPrime(n):
    while True:
        prime_num = nBitRandom(n)
        isCon = False
        
        for div in primes_list:
            if prime_num % div==0:
                isCon = True
                break
        
        if not isCon:
            return prime_num
        
        
def generators(n):
    while(True):
        a = random.randint(2, n-1) 
        if((n-1)%a != 1):
            return a


primes_list = [i+1 for i in range(1,1000)]
prime_list()
P = getnPrime(10)
print(P)
print(generators(P))
