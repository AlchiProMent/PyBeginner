from itertools import *

# генерация последовательности n-е число раз
lst = list( repeat(123,10) )
print(lst)

print( list( combinations('ABCD',2) ) )
print( list( permutations('ABCD',2) ) )
print( list( combinations_with_replacement('ABCD',2) ) )

# создать кортеж из последовательностей указанной размерности
matrix = tee([0,0,0,0,0],5)
for mtr in matrix:
    print( list(mtr) )


