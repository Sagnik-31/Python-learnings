def prime_factors(n):
    li= []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            li.append(divisor)
            n /= divisor
        else:
            divisor += 1
        
    print(li)
    
prime_factors(84)

            