"""Write a script that prompts the user for their phone number, x. Then carry out the following steps:
1. Compute x minus the sum of the digits of x. Call this result y. (hint: to find the sum of the digits of x, 
 check to see what x//10 and x%10 give you)
2. Compute the sum of the digits of y, and store the result back in y.
3. Repeat step 2 until y has just one digit, then display it."""


def compute_phone():
  x = input("What is your phone number? ")
  y = x - sum(int(digit) for digit in str(x))
  
  while y > 9:
    y = sum(int(digit) for digit in str(y))
  print y

compute_phone()
