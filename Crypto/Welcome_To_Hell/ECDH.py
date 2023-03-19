from elliptic_curve import ECPoint
from sympy.ntheory.modular import crt 
from sympy.ntheory import factorint
import time
import codecs

def ECDH(a, b, G):
  A = a*G
  B = b*G
  s1 = b*A
  s2 = a*B 
  assert s1 == s2, "Something's wrong, I can feel it"
  return s1

def inverseDL(P, Q, order):  
  R = ECPoint.identity()
  for i in range(order):
    if R == Q:
      return i 
    R += P
  return 0

def evaluatePrimePolynomial(values, prime):
  mod_prime = pow(prime, len(values))
  r = 0
  for i in range(len(values)):
    r += (values[i] * pow(prime, i)) % mod_prime
    r %= mod_prime
  return r

def pohligHellman(G, R, order):
  factors = factorint(order)
  # print(factors)
  v = []
  m = [ pow(prime, power) for (prime, power) in factors.items() ]
  for (prime, power) in factors.items():
    a = []
    for k in range(power):
      P = (order // prime) * G
      Q = (order // pow(prime, k+1)) * R 
      for r in range(k):
        T = ((order // pow(prime, k-r+1)) * a[r]) * G 
        Q -= T
      
      a.append(inverseDL(P, Q, prime))

    v.append(evaluatePrimePolynomial(a, prime))
    
  return crt(m, v, check=False)[0]

def bxor(bytes1, bytes2):
  return bytes([ b1^b2 for b1, b2 in zip(bytes1, bytes2)])

def function(bmsg, k):
  return bytes([(b^k) % 256 for b in bmsg])

def fiestel(bmsg, k):    
  l1 = bmsg[:16]
  r1 = bmsg[16:]
  
  l2 = r1
  r2 = bxor(l1, function(r1, k))
  return r2+l2
    
def main():
  # a = 52668 
  # b = 27292 
  
  ECPoint.a = 2
  ECPoint.b = 3
  ECPoint.p = 106859 #46349
  
  G = ECPoint(3, 6)
  R = ECPoint(81310, 85453)
  
  order = 53608
  
  encoded_flag = b"1+jn39uL7ZylzIrUzMicmEhlbGxAc0gxMnQtdGgxM30=\n"
  start = time.time()
  # assert R == ECDH(a, b, G), "Some error"

  # k = a*b % order
  k = pohligHellman(G, R, order) 
  
  flag_bytes = codecs.decode(encoded_flag, "base64")
  print(fiestel(flag_bytes, k))
  
  print("Time taken:", time.time()-start, "seconds")  
  
  
if __name__ == "__main__":
  main()