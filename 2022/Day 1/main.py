file = open('input.txt')
n = 1
max = 0
s = 0
while True:
  t = file.readline()
  if t=='\n':
    if s>max:
      max = s
    s = 0
    n+=1
  elif t!='':
    t = int(t)
    s+=t
  else:
    print(max)
    break
