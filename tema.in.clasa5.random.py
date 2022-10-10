from random import randint
n=int(input('dati nr de elemete:'))
lst=[]
suma=0
for i in range(n):
    lst.append(randint(1,100))
for i in lst:
     if i!=max(lst):
        suma+=i
print(lst)
print(suma)    