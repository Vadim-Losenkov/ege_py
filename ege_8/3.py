letters = 'МОИСЕЙ'
k = 0

for a in letters:
  for b in letters:
    for c in letters:
      for d in letters:
        word = a + b + c + d

        if word[0] != 'Й' and (word.count('О')>0 or word.count('И')>0 or word.count('Е')>0):
          k += 1

print(k)