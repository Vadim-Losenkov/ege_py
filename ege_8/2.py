letters = 'КАНТ'
k = 0

for a in letters:
  for b in letters:
    for c in letters:
      for d in letters:
        for e in letters:
          for f in letters:
            word = a + b + c + d + e + f

            if word.count('К') == 2:
              k += 1

print(k)