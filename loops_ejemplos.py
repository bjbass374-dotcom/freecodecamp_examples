def imprimir_titulo(tema):
     print(f"***************{tema}*******************************")


imprimir_titulo('LISTAS Y BUCLES')
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
     for letter in word:
          if letter.lower() in 'aeiou':
               print(f"'{word}' contains the vowel '{letter}'")
               break
     else:
          print(f"'{word}' has no vowels")

for num in range(40, -1, -10):
     print(num)

languages = ['Spanish', 'English', 'Russian', 'Chinese']
for index, language in enumerate(languages,1):
     print(f'Index {index} and language {language}')

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
     print(f'Name: {name}')
     print(f'ID: {id}')

#compresion de listas
imprimir_titulo('COMPRESION DE LISTAS')
even_numbers = []

for num in range(21):
     if num % 2 == 0:
          even_numbers.append(num)

print(even_numbers)

even_numbers1 = [num for num in range(21) if num % 2 == 0  ]
print(even_numbers1)

numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

#funcion filter()
imprimir_titulo('FUNCION FILTER')
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
     return len(word) > 4



long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']

#funcio map()
imprimir_titulo('FUNCION MAP')
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]

#FUNCIONES LAMBDA 
imprimir_titulo('FUNCIONES LAMBDA')
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]