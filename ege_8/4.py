letters = 'КОРНЕТ'
k = 0

for a in letters:
  for b in letters:
    for c in letters:
      for d in letters:
        for e in letters:
          word = a + b + c + d + e

          if word.count('О') <= 1 and word.count('Е') <= 1:
            k += 1

print(k)