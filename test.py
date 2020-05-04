#Napišite program, ki izpiše praštevila do 200

def prime(n):
    '''True False, NEUČINKOVIT'''
    for i in range(2, n):
        if not n % i:
            return False
    return True

def prastevila_do(n=200):
    '''izpise prastevila do n (200)'''
    for i in range(2, n):
        if prime(i):
            print(i, end=' ')

prastevila_do()