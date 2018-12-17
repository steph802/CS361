########################################################
#
#  Question 6
#
########################################################

#Function returns True only if n is prime
def is_prime(n) : 
    if (n < 2) : 
        return False
    if (n <= 3) : 
        return True

    if (n % 2 == 0 or n % 3 == 0) : 
        return False
   
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True 
  
#Function returns all primes up to n
def primesUpTo(n):
  for x in range(n): 
    if (is_prime(x)): 
      print(x)  

#Function returns first n primes
def firstNPrimes(n):
    primes = []
    x = 2
    while len(primes) != n:
      for i in range(2, x // 2 + 1):
        if x % i == 0:
          break
      else:
        primes.append(x)
      x += 1
    print(primes)
