# about lists
list = [12, 15, 16, -7, 22, 3, 0, 12]
print(list[2],"\n",list[-1],"\n",list[-3:],"\n",list[:3])
print(list)
print(list[:])
list += [3, 5, -12]
print(list)
print(3 in list)
# stack
list.append(100)
print(list)
x = list.pop()
print(list,"\t",x)
# queue
from collections import deque as queue
queue1 = queue([12,15])
x = queue1.popleft()
print(queue1,"\t",x)
# tuples
tup = {12,'a',5}
print(tup)
tup.add('b')
print(tup)
tup.discard(5)
print(tup)
# sets
ens = set([12,15,3])
print(ens)
a = set('hellooiiuy')
b = set('woorrlddf')
# shows the set without repeated letters
print(a,b)
list2=[a,b]
print(list2)
print(a-b)
print(a|b)
print(a^b)
# dictionnary
dict = {'key1':25,'key2':455}
print(dict)
print(dict['key1'])
for i in dict:
    print(dict[i])
print(dict.keys())
dict = {'key3':100}
print(dict)
# dictionnary using a math formula
dict2 = {x:x*3 for x in range(5)}
print(dict2)
n=3
for i in range(n):
    print(i)
j=0
while j <= 10:
    print(j)
    j+=1



