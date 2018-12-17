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

    
    
 ########################################################
#
#  Question 7
#
########################################################

#Function that prints all elements of a list
def listElements():
  myList = [1,2,3,4,5]
  print(myList)

#Function that prints all elements of a list in reverse
def reverseElements():
  myList = [1,2,3,4,5]
  print(myList[::-1])

#Function that returns number of elements in a list
def listLenght():
  myList = [1,2,3,4,5]
  print(len(myList))
    
    
    
    
 ########################################################
#
#  Question 8
#
########################################################    

def listEntries():
  a = [1,2,3,4,5]
  b = a
  b[1] = 8
  c = a[:]
  c[2] = 9
  print(a)
  print(b)
  print(c)

def set_first_elem_to_zero(l):
  l[0] = 0
  print (l)

myList = [1,2,3,4,5]
set_first_elem_to_zero(myList)





 ########################################################
#
#  Question 9
#
########################################################   

def mergeList(l):
  merged = [x for y in l for x in y]
  print (merged)

myList = [[1,3], [5,6]]
mergeList(myList)








 ########################################################
#
#  Question 11
#
########################################################   




 ########################################################
#
#  Question 12
#
########################################################   

def iteration(l):
    if len(l) != 0:
      product = 1
      for i in l:
          product *= i
    return product

def recursion(l):
    if len(l) == 1:
        return l[0]
    return recursion([l[0]]) * recursion(l[1:])

myList = [1,2,3,4,5]
print(iteration(myList))
print(recursion(myList))








 ########################################################
#
#  Question 13
#
########################################################   

import re
file = open('emails.txt', 'r')
file = file.read()

email = re.findall(r'([^ ]+[@][^ ]+[.][a-z]+)', file)
print(email)
