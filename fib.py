import time
def fib(m):

    if m==0 or m==1:
        return 1
    else:
        return fib(m-1)+fib(m-2)
start=time.time()
print(fib(20))
print(time.time()-start,'sec')
    
 
