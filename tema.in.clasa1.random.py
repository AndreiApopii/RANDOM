import random
n=int(input('dati nr de elemente:'))
spoz=0
sneg=0
for i in range(n):
    x=random.randint(-50,50)
    print(x)
    if x>0:
        spoz+=1
    if x<0:
        sneg+=1
print('spoz=', spoz)
print('sneg=', sneg)