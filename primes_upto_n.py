'''
given n , find prime numbers upto n.
'''

def generate_primes(n):
    primes=[]
    for num in range(1,n + 1):   
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)             
    return(primes)
