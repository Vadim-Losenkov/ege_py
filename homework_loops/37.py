# совершенные числа c пределом
number = int(input('Введите натуральное число: '))

for j in range(1, number):
  res = 0
  i = 1
  while j / i > 1:
    if j % i == 0:
      res += i

    i += 1

  if j == res:
    print(j)
