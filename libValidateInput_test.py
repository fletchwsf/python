# unit tests for libValidateInput
import libValidateInput

# Validate Input Greater (n,x) returns n if n > x
#    and returns False if n < x
def test_libValidateInputGreaterThan():
    assert  libValidateInput.greaterThan(1,0) == 1
    assert  libValidateInput.greaterThan(0,1) == False
    assert  libValidateInput.greaterThan(0,0) == False
    assert  libValidateInput.greaterThan(-1,0) == False
    assert  libValidateInput.greaterThan(-2,-1) == False
    assert  libValidateInput.greaterThan(-1,-2) == -1

# test case 1
#def testCase01():
#     if (assert libValidateInput.greaterThan(1,0) == 1):
#        print "testCase01 pass"
        