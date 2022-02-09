with open('17-243.txt') as f:
  s = [int(x) for x in f]

  res = []
  summ = 0

  for i in s:
    if i % 61 == 0:
      summ += sum(map(int, str(i)))

  for i in range(1, len(s)):
    if (s[i] > summ and not(s[i - 1] > summ)) and (str(s[i - 1])[-2:] == '33') or \
       (s[i - 1] > summ and not(s[i] > summ)) and (str(s[i])[-2:] == '33'):

       res.append(s[i] + s[i-1])

print(min(res), len(res))