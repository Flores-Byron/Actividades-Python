numero_secreto = 777
print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
numero = int(input("dime un numero: "))

while numero != numero_secreto:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero == numero_secreto
    print("¡Bien hecho, muggle! Eres libre ahora.")
