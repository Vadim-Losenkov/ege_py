def f(n):
  if n > 0:
    f(n - 3)
    print(n)
    f(n // 3)

print(f(9))