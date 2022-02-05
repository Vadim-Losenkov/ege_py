with open('17-4.txt') as f:
  s = [int(x) for x in f]

  res = []
  for i in s:
    if (str(i).count('0') >= 2) and (i % 7 == 0):
      res.append(i)

print(max(res), len(res))