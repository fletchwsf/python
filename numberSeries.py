# Calculate a Fibonacci series up to n
def Fibonacci(n):
 a = 0
 b = 1
 while b < n:
        print b,
        a, b = b, a + b
 
# Calculate Pie to n decimal places 3.1459
def Pie(n):
 a = 22
 b = 7
 result = []
 counter = 0
 while counter < n:
     remainder = a % b
     a = remainder 
     result.append(remainder)
     counter = counter + 1
 print result   

