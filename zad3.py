# Напишите программу удаляющую из текста все абв


my_str = ('lkdfgjadklgajlkзафоабв пфавповпоо абвдварпфавп абвалвыпоща Абв')
new_str = ' '.join(list(filter(lambda elem:'абв' not in elem.lower(), my_str.split())))  #  list, filter, lambda
print(new_str)