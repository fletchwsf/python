import libValidateInput
# ----------------------------------------------------------
# Calculate a Fibonacci series up to n
#
def Fibonacci(n):
    # check that user input n > 0
    #libValidateInput.greaterThan(n,0)
    a = 0
    b = 1
    while b < n:
        print b,
        a, b = b, a + b
#-----------------------------------------------------------

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

#------------------------------------------------------------
# Greatest common divisor (a,b) 
# call GCD(a,b)
# Find the greatest common divisor using Euclide's algorithm
#-----------------------------------------------------------
debug = False

def GCD(a_in,b_in):
    # use absolute value to avoid -1
    a = abs(a_in)
    b = abs(b_in)
    # if a < b swap places per the algorithm
    if ( a < b ):
        tmp = a
        a = b
        b = tmp
    
    # one last sanity check
    if ( (a < 1) or ( b < 1)):
        print "enter values greater than zero!"
        return False
    
    # subtract as many multiples of b from a as possible
    # as long as the remainder is > b
    multiple = 0
    remainder = b
    while (remainder >= b):
        remainder = a - b * multiple
        multiple += 1
                
    # if the remainder is zero then b is the GCD, otherwise 
    # update b with the value of the remainder and a with the
    # value of b and repeat
    if (remainder == 0):
        if debug:
            print "found GCD value of:" + str(b)
        return (b)
    # else
    a = b
    b = remainder
    GCD(a,b)
        
        
    