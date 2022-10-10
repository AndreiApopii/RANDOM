from random import randint
x=[]
for i in range (1):
    y=randint(0,999999999)
    print(y)
while y>0:
    r=y%10
    y//10
    x.append(r)
print('0 apare de:', x.count(0), 'ori')
print('1 apare de:', x.count(1), 'ori')
print('2 apare de:', x.count(2), 'ori')
print('3 apare de:', x.count(3), 'ori')
print('4 apare de:', x.count(4), 'ori')
print('5 apare de:', x.count(5), 'ori')
print('6 apare de:', x.count(6), 'ori')
print('7 apare de:', x.count(7), 'ori')
print('8 apare de:', x.count(8), 'ori')
print('9 apare de:', x.count(9), 'ori')
