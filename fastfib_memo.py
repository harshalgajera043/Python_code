def fastFib(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        print("Memo[" ,n, "]:", memo[n])
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result
n=int(input('Enter a number for fibonacci: '))

for i in range(n+1):
    print('fib of', i, '=', fastFib(i))
    
