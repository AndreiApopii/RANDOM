from random import randint 
def divizibil6si8():
    numar = randint(100,999)
    while(numar%6!=0 or numar%8!=0):
        numar = randint(100,999)
    return numar
print(divizibil6si8())