b =  (i**2 for i in range(1,10))
a = 0
# while a<5:
   # print(next(b))
   # a += 1 
# print(list(b)) ## sax mianqamic tppuma listi mej
# print(sum(b)) ## tpuma meji sax arjeqneri gumary
# print(next(b)) ## araji angam greluc tpuma 1 elementy heto amen hajordy

def genf():
   s = 7
   for i in [43,65,32, 88,8]:
      yield i
      print(s)
      s=s*10+7
g = genf()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))