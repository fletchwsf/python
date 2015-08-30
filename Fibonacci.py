# Python 3: Fibonacci series up to n
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    print(result)
    
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
