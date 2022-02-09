string = input('Введите число: ')

if len(string) > 1:
  lastSymbol = string[len(string) - 1]
  startSymbol = string[0]

  print(lastSymbol + string[1:][:-1] + startSymbol)