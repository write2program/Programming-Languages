num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print("Factorial does not exist for negative numbers")
elif num == 0:
   print("Factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("Factorial of",num,"is",factorial)
"""
Output: 
Enter a number: 5
Factorial of 5 is 120
"""
