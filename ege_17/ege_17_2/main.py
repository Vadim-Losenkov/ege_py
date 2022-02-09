with open('17-205.txt') as f:
  s = [int(x) for x in f]

  res = []

  for i in range(1, len(s)):
    if (abs(s[i]) % 10 == 7 or abs(s[i-1]) % 10 ==  7) and (s[i] + s[i-1]) % 12 == 0:
      res.append(s[i] + s[i-1])

print(max(res), len(res))