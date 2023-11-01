def getNthFib(n):
    # Write your code here.
    if n == 2:
        return 1
    if n == 1:
        return 0
    answer = getNthFib(n-1) + getNthFib(n-2)
    return answer


def getNthFib(n, memoization={1:0, 2:1}):
    # Write your code here.
    if n in memoization:
        return memoization[n]
    else:
        memoization[n] = getNthFib(n-1, memoization) + getNthFib(n-2, memoization)
        return memoization[n]
    

def getNthFib(n):
    # Write your code here.
    if n == 1:
        return 0
    if n == 2:
        return 1
    fib = [0,1]
    counter =  3
    while counter <= n:
        new_fib = fib[0] + fib[1]
        fib.append(new_fib)
        fib.pop(0)
        counter = counter + 1
    return fib[1]
