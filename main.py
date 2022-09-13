# 1. Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.

import datetime

def logger(func):
  
  def new_func(*args, **kwargs):
    start = str(datetime.datetime.now())
    result = func(*args, **kwargs)
    print(args)
    print(kwargs)
    with open('file_exit.txt', "w") as file:
      file.write(f'Дата и время вызова функции: {start}\n')
      file.write(f'Имя функции: {func.__name__}\n')
      file.write(f'Аргументы функции: {args} и {kwargs}\n')
      file.write(f'Возвращаемое значение функции: {result}')
    return result

  return new_func

@logger
def calc(a, b):
  sum = a + b
  return sum

sum = calc(2, b=5)

print(sum)


# 2. Написать декоратор из п.1, но с параметром – путь к логам.

# from pathlib import Path  
import os

def logger2(path):

  def logger(func):
  
    def new_func(*args, **kwargs):
      start = str(datetime.datetime.now())
      result = func(*args, **kwargs)
      print(args)
      print(kwargs)
      with open(path, "w") as file:
        file.write(f'Дата и время вызова функции: {start}\n')
        file.write(f'Имя функции: {func.__name__}\n')
        file.write(f'Аргументы функции: {args} и {kwargs}\n')
        file.write(f'Возвращаемое значение функции: {result}')
      return result

    return new_func
    
  return logger

# path = Path("fold", "file_exit.txt") 

path = os.path.join(os.path.join(os.getcwd(), 'fold'), 'file_exit.txt')
@logger2(path)
def calc(a, b):
  sum = a + b
  return sum

sum = calc(2, b=5)

print(sum)


# 3. Применить написанный логгер к приложению из любого предыдущего д/з.

# see prehomework.py function commander



