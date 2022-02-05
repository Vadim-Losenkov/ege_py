def f(n):
  if (n == 1) or (n == 2):
    return n
  else:
    return 2 * f(n - 1) + (n - 2) * f(n - 2)

print(f(6))