class nector:
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k
 
  def __str__(self):
    return f"the vector is: {self.i}i + {self.j}j + {self.k}k"
  def __add__(self, other):
    return nector(self.i + other.i, self.j + other.j, self.k + other.k)
    
    
v = nector(1,2,3)
print(v)  
v2 = nector(4,5,6)
print(v2)
print(nector.__add__(v,v2))
