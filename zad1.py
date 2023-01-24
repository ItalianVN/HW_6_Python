# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


with open('text.txt', 'w') as f:         
    f.write('1 2 3 4 5 6 8 9 10 \n')        
    f.write('78 79 80 81 \n')

path = 'text.txt'                       
data = open(path, 'r')
num_row = []                             
for line in data:                        
    print(line)
    num_row += list(map(int, line.split()))              # разделили все данные по пробелу, перевели все в инт с помощью map,обявили все в лист,
                                                        # т.к. функуия map возвращает значения инт,+= соединяет строки
data.close()
print(num_row)

for i, elem in enumerate(num_row[:-1]):                  #использовали enumerate                     
    if elem + 1 != num_row[i+1]:                   
        print(elem+1)
        break
