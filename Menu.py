# Matriz del menú
menu = [
    ["Hamburguesa", "Comida Rapida", 18000],
    ["Pizza", "Italiana", 36000],
    ["Ensalada Cesar", "Saludable", 22000],
    ["Jugo Natural", "Bebida", 8000],
    ["Pasta Alfredo", "Italiana", 30000],
    ["Lasagna", "Italiana", 28000]
]

# Función para calcular el precio final
def calcular_precio_final(categoria, precio_base):
    
    categoria_objetivo = "Italiana"
    umbral_precio = 25000

    # Aplicar descuento del 15%
    if categoria == categoria_objetivo and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base

    return precio_final


# Mostrar resultados
print("MENÚ DEL RESTAURANTE")
print("-" * 50)

for producto in menu:
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(categoria, precio_base)

    print(f"Producto: {nombre}")
    print(f"Categoría: {categoria}")
    print(f"Precio base: ${precio_base}")
    print(f"Precio final: ${precio_final}")
    print("-" * 50)