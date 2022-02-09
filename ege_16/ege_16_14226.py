def F(n):
  if n > 2:
    return F(n - 1)+ G(n - 2)
  else: return n+1
 
def G(n):
  if n > 2:
    return G(n - 1)+ F(n - 2)
  else: return n

print(F(7))