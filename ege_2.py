print('x y z w') # выводим данные в задаинии переменные

for x in range(2): # перебираем каждую переменную через in range(2)
  for y in range(2):
    for z in range(2):
      for w in range(2):
        # пишем условие указанное в задании
        if (((x <= y) and (y <= w)) or (z == (x or y))) == 0:

          # выводим пременный в том же порядке, что и в начале
          print(x, y, z, w)
