from Crypto.Cipher import AES
import hashlib
import codecs

def mod_pow(x, y, p):
  r = 1
  for i in range(y):
    r = (r * x) % p
  return r % p 

def diffie_hellman(p, g, a, b):
  A = mod_pow(g, a, p)
  B = mod_pow(g, b, p)
  print("A: ", A)
  print("B: ", B)
  s1 = mod_pow(B, a, p)
  s2 = mod_pow(A, b, p)
  return hashlib.sha256(str(s1).encode('utf-8')).digest()

def possible_keys(p, g, order, shared_secret):
  r = 1
  for i in range(order):
    r = (r * g) % p
    if hashlib.sha256(str(r).encode('utf-8')).digest() == shared_secret:
      print("Key found")
      return 
  print("Key not found")

def find_order(g, p):
  r = 1
  for i in range(1, p-1):
    r = (r * g) % p
    # print(r)
    if r == 1:
      # print("Order found:", i)
      return i
  # print("Order not found")
  
def encrypt(plaintext, key):
  cipher = AES.new(key, AES.MODE_ECB)
  return cipher.encrypt(plaintext)

def decrypt(ciphertext, key):
  cipher = AES.new(key, AES.MODE_ECB)
  return cipher.decrypt(ciphertext)

def looks_like_flag(plaintext):
  if plaintext[:4] == "WEC{" and plaintext[-1] == "}":
    return True 
  return False

def get_flag(g, p, ciphertext):
  r = 1
  for i in range(1, find_order(g, p)):
    r = (r * g) % p 
    ck = hashlib.sha256(str(r).encode('utf-8')).digest()
    
    plaintext = decrypt(ciphertext, ck)
    if  looks_like_flag(plaintext.decode('utf-8', errors="ignore")):
      return plaintext.decode('utf-8', errors='ignore')   
    

# flag = "WEC{DH_sm@a11_subgr0up_A11@ck-c@N-Be-Pr3v3ntedD}"
flag = "lZyiOdb3KVLrsCn4rOZ3PJ36SCJAnRVGfq4sv4jkFw2TIPiSPHcr5Kv5l/w3Nc9W\n"
e_flag = codecs.decode(flag.encode('utf-8'), 'base64')
# print(e_flag)
p = 1300433
g = 16
# order = find_order(g, p)

# print(order)

# a = 607539
# b = 913127
# print("a =", a)
# print("b =", b)


# shared_secret = diffie_hellman(p, g, a, b)
# print("Shared secret:", shared_secret)

# possible_keys(p, g, order, shared_secret)

# print("Encrypted flag:", codecs.encode(encrypt(bytes(flag, 'utf-8'), shared_secret), 'base64'))

print(get_flag(g, p, e_flag))