file = open('input.txt')
def Part_1():
  q = 0
  for y in file.readlines():
    y = y.split('x')
    sa = 2*(int(y[0])*int(y[1]))+(2*(int(y[1])*int(y[2])))+(2*(int(y[0])*int(y[2])))
    l = []
    l.append(int(y[0])*int(y[1]))
    l.append(int(y[0])*int(y[2]))
    l.append(int(y[1])*int(y[2]))
    q+=(sa+min(l))
  print("Answer for Part 1:",q)
def Part_2():
  file.seek(0)
  z = 0
  for i in file.readlines():
    i = i.split('x')
    i = list(map(int,i))
    a = i.copy()
    wrap = 0
    wrap+=(min(i)*2)
    i.remove(min(i))
    wrap+=(min(i)*2)
    z += wrap+(a[0]*a[1]*a[2])
  print("Answer for Part 2:",z)


Part_1()
Part_2()
