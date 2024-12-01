#open file
f = open('input_1.txt','r')
lines = f.readlines()
list_1 = []
list_2 = []
for line in lines:
    words = line.strip().split(' ')
    list_1.append(words[0])
    list_2.append(words[-1])

distances = []
n=len(list_1)
while n>0:
    distances.append(abs(min(list_1)-min(list_2)))
    del list_1[list_1.index(min(list_1))]
    del list_2[list_2.index(min(list_2))]
    n-=1
print(sum(distances))