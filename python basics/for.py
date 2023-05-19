#Цикл for проходится по элементам любого итерируемого объекта (строки, списка и т.д.) 
# и во время каждого прохода выполняет заданную последовательность действий.

iterator = [1, 2, 3, 4 ,5]

for value in iterator:
    pass
    #блок кода с телом цикла

#for i in range(start, stop, step):

# итерация по строкам
company_name = 'SkillFactory'
# мы сами задаем имя переменной в которую будут последовательно помещаться каждый элемент нашего объекта
for letter in company_name: 
    letter = letter.upper()
    print('*', letter, '*', sep='', end='')

# Операторы break и continue
#break – прерывает исполнение цикла  
#continue – прерывает только текущую итерацию и сразу переходит к следующей  
#Работают и с while, и с for

phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
for letter in phrase:
    if letter == ' ':
        continue
    print(letter, end='')

