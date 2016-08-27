def find_sum(n):
    #return (n*(n+1))/2
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum