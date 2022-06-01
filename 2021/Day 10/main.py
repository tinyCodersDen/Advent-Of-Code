file = open('input.txt')
endings = [')',']','}','>']
startings = ['(','[','{','<']
dict1 = {')':1,']':2,'}':3,'>':4}
l = []
score = 0
final = []
incomplete_lines = []
for t in file.readlines():
  incomplete_lines.append(t.strip())
  for y in t.strip():
    if y not in endings:
        l.append(endings[startings.index(y)])
    else:
      if y==l[-1]:
        l.pop(-1)
      else:
        incomplete_lines.pop(-1)
        l = []
        break
l = []
for z in incomplete_lines:
  for a in z:
    if a not in endings:
      l.insert(0,endings[startings.index(a)])
    else:
      if a==l[0]:
        l.pop(0)
  score = 0
  for sf in l:
    score = score*5
    score+=dict1[sf]
  final.append(score)
  l = []
final.sort()
print(final[(len(final)-1)//2])
