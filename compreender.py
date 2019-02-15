#!/usr/bin/python3

#grep - RHn split

duck_tails = ['Huguinho|1', 'Zezinho|2', 'Luizinho|3']
#for d in duck_tails:
 #   print(d.split('|')[0]) 


# forma mais direta para resolver
# ['Huguinho|1', 'Zezinho|2', 'Luizinho|3']

#for d in [i.split('|')[0] for i in duck_tails]:

#escrever a primeira e a ultima letra de cada nome
#for d in [i.split('|')[0] for i in duck_tails]:
#    print(d[0], d[-1])

#não escrever quando o nome for zezinho
#for d in [i.split('|')[0] for i in duck_tails if 'Zezinho' not in i]:
# print(d[0], d[-1])


#for d in [i.split('|')[0] for i in duck_tails if 'Zezinho' not in i]:
# print(d[0], d[-1])

#def double(i):
#    return i*2

for n in map(lambda i : i * 2, [1,2,3,4]):
    print(n)



