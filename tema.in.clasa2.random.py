from random import randint
n=int(input('dati nr de aruncari:'))
k=0
for x in range (n):
    y=randint(1,6)
    print(y)
    if y==6:
        k+=1
print('valoarea 6 a aparut de:', k, 'ori')
