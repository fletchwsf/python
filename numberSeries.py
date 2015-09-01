# Calculate a Fibonacci series up to n
def Fibonacci(n):
 a = 0
 b = 1
 while b < n:
        print b,
        a, b = b, a + b
 
# Calculate Pie to n decimal places 3.1459...
def Pie(n):
 result = []
 a = 22
 b = 7
 counter = 0
 while counter < n:
     result.append(a/b)
     remainder = a % b
     a = remainder * 10
     counter = counter + 1
 print result   

