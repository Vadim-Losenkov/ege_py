# Числа Армстронга
for j in range(100, 10000):
  armstr = 0
  mapObj = map(int, str(j))

  for i in mapObj:
    armstr += i**(len(str(j)))

  if armstr == j:
    print(j)
