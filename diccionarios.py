def imprimir_titulo(tema):
     print(f"***************{tema}*******************************")

imprimir_titulo('ITERACION SOBRE DICCIONARIOS')

products = {
     'Laptop': 990,
     'Smartphone': 600,
     'Tablet': 250,
     'Headphones': 70,
}

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)

imprimir_titulo('USO DE ENUMERATE')

for product in enumerate(products):
     print(product)

for index, product in enumerate(products):
     print(index, product)

for price in enumerate(products.values()):
     print(price)

for index, price in enumerate(products.values()):
     print(index, price)

for index, product in enumerate(products.items()):
     print(index, product)

for index, product, price in enumerate(products.items()):
     print(index, product, price)