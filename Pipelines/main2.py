import sys

# получение символов их входного потока
s = sys.stdin.read()

# разбиение на отдельные числа в виде цифровых строк
lst = s.split(',')

# суммирование всех чисел
summa=sum(map(int,lst))

# передача в выходной поток строки вида "summa = XX"
sys.stdout.write(f'summa = {summa}')
