# перебираем варианты через цикл, желательно выбрать число побольше
# что бы данное в задание число попало в диапазон
for i in range(1, 150): 
  # переводим число i в двоичную систему и превращаем его в с троку
  n = str(bin(i))[2:] # записью [2:] мы избавляемся от 2х лишних сиволов в начале строки, которые нам генерирует python
  
  # метод count подсчитывает сколько раз повторяется аргумент (который мы укажем) в сторке
  # в нашем случае мы считаем кол-во 1 в строке
  if n.count('1') % 2 == 0:
    n += '00'
  else:
    n += '11'
  if int(n, 2) > 114:
    print(i)
    break