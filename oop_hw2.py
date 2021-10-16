class Triangle:
   def __init__(self, side_1, side_2, side_3):
      self.side_1 = side_1
      self.side_2 = side_2
      self.side_3 = side_3
   
   def perimeter(self):
      return self.side_1 + self.side_2 + self.side_3
   
   def area(self, *args, **kwargs):
      s = (self.side_1 + self.side_2 + self.side_3) / 2
      area_ = (s*(s-self.side_1)*(s-self.side_2)*(s-self.side_3)) ** 0.5
      return area_
   
   def __call__(self, *args, **kwargs):
      return self.perimeter(), self.area()
   
   def __eq__(self, other):
      if self.side_1 == other.side_1 and self.side_2 == other.side_2 and self.side_3 == other.side_3 or\
         self.side_1 == other.side_2 and self.side_2 == other.side_1 and self.side_3 == other.side_3 or\
         self.side_1 == other.side_3 and self.side_2 == other.side_1 and self.side_3 == other.side_2 or\
         self.side_1 == other.side_1 and self.side_2 == other.side_3 and self.side_3 == other.side_1 or\
         self.side_1 == other.side_2 and self.side_2 == other.side_3 and self.side_3 == other.side_1 or\
         self.side_1 == other.side_3 and self.side_2 == other.side_2 and self.side_3 == other.side_1:
            return "These triangles are equal"
      else:
         raise ValueError("These trangles are not equal")
triangle_0 = Triangle(3, 4, 5)
triangle_1 = Triangle(5, 4, 3)
print(triangle_0())
print(triangle_0 == triangle_1)