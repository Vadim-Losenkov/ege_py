def f(n):
  if n == 1:
    return 1
  elif n > 2:
    return f(n - 2) * n
  else:
    return '_'

print(f(7))