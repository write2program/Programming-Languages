num = int(input("Enter a number to find sum : "))
if num < 0:
   print("Enter a number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
"""
Enter a number to find sum : 15
The sum is 120
"""

