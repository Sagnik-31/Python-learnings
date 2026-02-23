def is_perfect(n): 
    divisors_sum = 0
    for i in range(1,n):
        if n%i == 0:
            divisors_sum += i

    if divisors_sum == n:
        return True
    else:
        return False
print(is_perfect(28))
    