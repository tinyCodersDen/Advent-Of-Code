file = open('input.txt')
c = 0
c2 = 0
while True:
    k = file.readline().strip().split(',')
    if k==['']:
        break
    k1,k2 = k[0].split('-'),k[1].split('-')
    if (int(k1[0])<=int(k2[0]) and int(k1[1])>=int(k2[1])) or (int(k2[0])<=int(k1[0]) and int(k2[1])>=int(k1[1])):
        c+=1
    if (int(k1[0])<=int(k2[0])<=int(k1[1]) or int(k1[0])<=int(k2[1])<=int(k1[1])) or (int(k2[0])<=int(k1[0])<=int(k2[1]) or int(k2[0])<=int(k1[1])<=int(k2[1])):
        c2+=1
print('Answer to Part 1:',c)
print('Answer to Part 2:',c2)
