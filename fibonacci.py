# -*- coding: utf-8 -*-
# fibonacci sequence

def fib(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else: 
        return fib(n-2) + fib(n-1)

n = 0

end = 20 #number to finish

while n < end:
    print(fib(n))
    n += 1
    
		
