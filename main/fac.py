"""Write a script to compute how many unique prime factors an integer has.  
For example, 12 = 2 x 2 x 3, so has two unique prime factors, 2 and 3. 
Use your script to compute the number of unique prime factors of 1234567890."""

def fac(i):
  factors = []
  print "Starting number is ", i
  f = 2

  while i <> 1:
    while i % f == 0:
      i /= f
      factors.append(f)
      print "adding factor ", f, ", new number ", i
    f += 1
  
  factors.sort()
  print "Here are the factors: ", factors

fac(1234567890)
