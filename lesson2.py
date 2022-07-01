totalHours = int(input('Сколько часов проходит наблюдение: '))
cells = 1

for hour in range(1, totalHours // 3 + 1):
  cells *= 2
  print('Прошло часов: ', hour * 3)
  print('Клеток: ', cells)
  print('Часов до конца эксперимента: ', totalHours - hour * 3)
  print()
print('Наблюдение закончилось')