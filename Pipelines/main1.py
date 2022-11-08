import sys

try:
	# чтение файла 'datas.txt'
	with open('datas.txt') as f:
		s_in = f.read()
except OSError:
	print('Ошибка при чтении файла!')
else:
	# передача в выходной поток прочитанных данных
	sys.stdout.write(s_in)



