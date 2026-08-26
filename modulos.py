def imprimir_titulo(tema):
     print(f"***************{tema}*******************************")

imprimir_titulo("MODULOS, USO Y TRABAJO")

from math import radians, sin, cos

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(round(sine_value,2)) # 0.6427876096865393
print(cos_value)  # 0.766044443118978

import datetime
birthday = datetime.date(1959, 7, 15)
print(birthday.day)    # 15
print(birthday.month)  # 7
print(birthday.year)   # 1959

imprimir_titulo("USO DE __name__")
# app.py
import utilidades  # Aquí importamos el módulo
print("Dentro de app.py")
print(f"Mi __name__ es: {__name__}")