def apply_discount(price,discount):
     if not (isinstance(price,int) or isinstance(price,float)):
          return "The price should be a number"
     elif not (isinstance(discount,int) or isinstance(discount,float)):
          return "The discount should be a number"
     elif price<=0:
          return "The price should be greater than 0"
     elif discount<0:
          return "The discount should be between 0 and 100"
     else:
          final_price=price-price*discount/100
          return final_price

print(apply_discount(0,60))


def caesar(text, shift, encrypt=True):

     if not isinstance(shift, int):
          return 'Shift must be an integer value.'
     if shift < 1 or shift > 25:
          return 'Shift must be an integer between 1 and 25.'

     alphabet = 'abcdefghijklmnopqrstuvwxyz'

     if not encrypt:
          shift = - shift
          shifted_alphabet = alphabet[shift:] + alphabet[:shift]
          translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
          encrypted_text = text.translate(translation_table)
          return encrypted_text

def encrypt(text, shift):
     return caesar(text, shift)

def decrypt(text, shift):
     return caesar(text, shift, encrypt=False)

#encrypted_text = encrypt('freeCodeCamp', 3)
encrypted_text="Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text=decrypt(encrypted_text,13)
print(decrypted_text)


#ejercicio para crear un personaje con barra de atributos 
full_dot = '●'
empty_dot = '○'

def create_character(name,strength,intelligence,charisma):
     if not isinstance(name,str):
          return "The character name should be a string"
     elif not name:
          return "The character should have a name"
     elif len(name)>10:
          return "The character name is too long"
     elif " " in name:
          return "The character name should not contain spaces"
     elif not isinstance(strength,int) or not isinstance(intelligence,int) or not isinstance(charisma,int):
          return "All stats should be integers"
     elif strength<1 or intelligence <1 or charisma<1:
          return "All stats should be no less than 1"  
     elif strength>4 or intelligence >4 or charisma>4:
          return "All stats should be no more than 4"
     elif not strength+intelligence+charisma==7:
          return "The character should start with 7 points"
     else:
          str_points=full_dot*strength+empty_dot*(10-strength)
          int_points=full_dot*intelligence+empty_dot*(10-intelligence)
          cha_points=full_dot*charisma+empty_dot*(10-charisma)
          return name+"\nSTR "+str_points+"\nINT "+int_points+"\nCHA "+cha_points


print(create_character('Bryan',1,4,2))



#ejercicio para crear un personaje con barra de atributos con alternativa de bucle for
def create_character2(name, strength, intelligence, charisma):
     # (Tus validaciones están perfectas, las dejamos exactamente igual)
     if not isinstance(name, str):
          return "The character name should be a string"
     elif not name:
          return "The character should have a name"
     elif len(name) > 10:
          return "The character name is too long"
     elif " " in name:
          return "The character name should not contain spaces"
     elif not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
          return "All stats should be integers"
     elif strength < 1 or intelligence < 1 or charisma < 1:
          return "All stats should be no less than 1"  
     elif strength > 4 or intelligence > 4 or charisma > 4:
          return "All stats should be no more than 4"
     elif strength + intelligence + charisma != 7:
          return "The character should start with 7 points"
     else:
          # Función interna que construye la barra de estadísticas USANDO UN BUCLE FOR
          def build_stat_bar(value):
               # Paso 1: Creamos una lista con 10 puntos vacíos (mutables)
               points = [empty_dot] * 10  
               
               # Paso 2: Bucle for para reemplazar los primeros 'value' elementos
               # Como value siempre será entre 1 y 4 (por tus validaciones), 
               # jamás dará error de índice fuera de rango.
               for i in range(value):
                    points[i] = full_dot   # Ahora sí, modificamos la lista
               
               # Paso 3: Unimos la lista en un solo string y lo devolvemos
               return ''.join(points)

     # Construimos las 3 barras usando el bucle for
     str_points = build_stat_bar(strength)
     int_points = build_stat_bar(intelligence)
     cha_points = build_stat_bar(charisma)

     return name + "\nSTR " + str_points + "\nINT " + int_points + "\nCHA " + cha_points

# Prueba
print(create_character2('Bryan', 1, 4, 2))

developer = 'Naomi'

result = developer.endswith('N') # ?
print(result)

def greet():
     pass

print(greet()) # ?

developer = 'Jessica'

print(developer.upper()) # JESSICA

x=6.581
print(round(x,2))
print(floor(x))