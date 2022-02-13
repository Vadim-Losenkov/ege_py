letters = 'ABCDX'
k = 0

for a in letters:
  for b in letters:
    for c in letters:
      for d in letters:
        word = a + b + c + d

        if word.count('X') == 1:
          k += 1

print(k)