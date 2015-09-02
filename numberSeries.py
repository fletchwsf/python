# ----------------------------------------------------------
# Calculate a Fibonacci series up to n
#
def Fibonacci(n):
    a = 0
    b = 1
    while b < n:
        print b,
        a, b = b, a + b


#-----------------------------------------------------------
# Calculate Pie to n decimal places 3.1459...
#  
def Pie(n):
    result = []   # an array to accumulate the answer
    numerator = 22
    denominator = 7
 
    counter = 0
    while counter < n:
        # depends on the use integer math
        result.append(numerator/denominator)
        remainder = numerator % denominator
        # move decimal to the right
        numerator = remainder * 10
        counter = counter + 1
    print result
    
#------------------------------------------------------------