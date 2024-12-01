from collections import Counter

def get_lists():  
    #open file
    f = open('input_1.txt','r')
    lines = f.readlines()
    list_1 = []
    list_2 = []
    for line in lines:
        words = line.strip().split(' ')
        list_1.append(int(words[0]))
        list_2.append(int(words[-1]))
    return list_1,list_2
list_1,list_2 = get_lists()
distances = []
n=len(list_1)
while n>0:
    distances.append(abs(min(list_1)-min(list_2)))
    del list_1[list_1.index(min(list_1))]
    del list_2[list_2.index(min(list_2))]
    n-=1
print('answer 1: ',sum(distances))
# puzzle 2
list_1,list_2 = get_lists()
elements_1 = set(list_1) 
counter_2 = Counter(list_2)
similarity = 0

for el in elements_1:
    similarity += el*counter_2[el]
print('answer 2: ',similarity)