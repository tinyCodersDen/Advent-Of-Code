file = open('input.txt')
def Part_1():
  c = 0
  for y in file.readline():
    if y=='(':
      c+=1
    elif y==')':
      c-=1
  print('Answer for Part 1:',c)
def Part_2():
  c = 0
  file.seek(0)
  for e,y in enumerate(file.readline()):
    if y=='(':
      c+=1
    elif y==')':
      c-=1
    if c<0:
      print('Answer for Part 2:',e+1)
      break

Part_1()
Part_2()
