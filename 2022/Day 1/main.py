file = open('input.txt')
n = 1
l = []
s = 0
while True:
  t = file.readline()
  if t=='\n':
    l.append(s)
    s = 0
    n+=1
  elif t!='':
    t = int(t)
    s+=t
  else:
    break
l.sort()
print('Answer to Part 1:',l[-1])
print('Answer to Part 2:',l[-1]+l[-2]+l[-3])
