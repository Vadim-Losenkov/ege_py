# Автоморфные числа
from math import sqrt
number = int(input('Введите число: '))
conditionNumber = lambda num: int(str(num)[-len(str(round(sqrt(num)))):])

for i in range(1, number):
  if round(sqrt(i)) == conditionNumber(i) and conditionNumber(i)**2 == i:
    print(i, round(sqrt(i)))
