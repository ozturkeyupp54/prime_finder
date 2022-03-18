# prime_finder
A function that outputs all prime numbers from 1 to n (including n).

def prime_finder(a):
  number= int(a)
  results = []
  for i in range(2,number+1):
    divisors= []
    for j in range(1,i):
      if i % j == 0:
        divisors.append(j)
    if len(divisors) < 2 :
      results.append(i)
  print(results)
