import numpy as np

class ECPoint:
  p = 0
  a = 0
  b = 0
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  @property
  def get_x(self):
    return self.x 
  
  @property
  def get_y(self):
    return self.y 

  @classmethod
  def powmod(cls, x, y):
    r = 1
    for i in range(y):
      r = (r * x) % ECPoint.p
    return r 
  
  @classmethod
  def modinv(cls, x):
    return ECPoint.powmod(x, ECPoint.p-2)
  
  @classmethod
  def identity(cls):
    return ECPoint(np.inf, np.inf)
    
  def is_identity(self):
    return self.x == np.inf and self.y == np.inf
    
  def _double_point(self):
    if self.is_identity():
      return self  
    
    if (self.y == 0):
      return ECPoint.identity()
    
    m = ((3*self.x**2 + ECPoint.a) * ECPoint.modinv(2*self.y)) % ECPoint.p
    new_x = (m**2 - 2*self.x) % ECPoint.p  
    new_y = (m*(self.x - new_x) - self.y) % ECPoint.p
    return ECPoint(new_x, new_y)
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __neg__(self):
    return ECPoint(self.x, -self.y)
  
  def __add__(self, other):
    if self.is_identity():
      return other 
    
    if other.is_identity():
      return self 
    
    if self == other:
      return self._double_point()
    
    if self.x == other.x:
      return ECPoint.identity()
    
    m = ((other.y - self.y) * ECPoint.modinv(other.x - self.x)) % ECPoint.p
    # print(m)
    # print(self, other)
    new_x = (m**2 - self.x - other.x) % ECPoint.p
    new_y = (m*(self.x - new_x) - self.y) % ECPoint.p 
    return ECPoint(new_x, new_y)
  
  def __iadd__(self, other):
    return self + other
    
  def __rmul__(self, n):    
    temp_point = ECPoint(self.x, self.y) 
    result = ECPoint.identity()
    while n != 0:
      if n & 1:
        result += temp_point
        
      temp_point = temp_point._double_point()
      n >>= 1
    return result
  
  def __imul__(self, n):
    return n * self
  
  def __sub__(self, other):
    return self + (-other)
  
  def __isub__(self, other):
    return self - other
  
  @property
  def order(self):
    R = ECPoint.identity()
    i = 1
    while True:
      R += self 
      if R.is_identity():
        break
      i += 1
    return i
  
  def __str__(self):
    s = "Point ({}, {})".format(self.x, self.y)
    return s

if __name__ == "__main__":
  ECPoint.a = -7
  ECPoint.b = 10
  ECPoint.p = 17
  
  P = ECPoint(1,2)
  Q = ECPoint(5,8)
  
  print(P+Q)
  print((P+Q)-Q)