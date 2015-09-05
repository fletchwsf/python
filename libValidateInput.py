#------------------------------------------------------------
# Range checks
#------------------------------------------------------------

# check for n greater than (x)
def greaterThan(n,x):
    if ( n > x):
        return n
    #else
    print "You entered:" + str(n)
    print "Enter value greater than:" + str(x)
    return False 

# check for n between (x,y)
def rangeBetween(n,x,y ):
    if ( (x < n) and ( n < y) ):
        return(n)
    #else
    print "You entered:" + str(n)
    print "Enter value between " + str(x) +  " and " + str(y)
    return False

#------------------------------------------------------------
# Type checks

# check for integer type


