# совершенные числа
number = int(input('Введите число: '))
res = 0

if number > 0:
  i = 1
  while number / i > 1:
    if number % i == 0:
      res += i

    i += 1

  if number == res:
    print(f'Число "{number}" Совершенное')
  else:
    print(f'Число "{number}" не является совершенным')

else:
  print(f'Число "{number}" не является натуральным')