numbersArr = []
summ = 0
product = 1

for i in range(10):
  numbersArr.append(int(input(f'Введите число №{i+1}: ')))

for i in range(len(numbersArr)):
  summ += numbersArr[i]
  product *= numbersArr[i]

print(f'\nСумма введенных числел: {summ} \nПроизведение введенных числел: {product}')