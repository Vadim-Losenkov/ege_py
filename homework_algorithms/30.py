numbersArr = []

print('Для остановки программы введите 0 \n\n')

i = ''
while i != 0:
  i = int(input(f'Введите число: '))
  if i: numbersArr.append(i)

print(f'\nМаксимальное число: {max(numbersArr)} \nМинимальное число: {min(numbersArr)}')