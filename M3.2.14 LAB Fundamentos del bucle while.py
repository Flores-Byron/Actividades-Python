blocks = int(input("Ingresa el número de bloques: "))

# Paso 2: inicializar variables
height = 0
layer = 1

# Paso 3: construir capa por capa
while blocks >= layer: # usar los bloques necesarios para la capa actual
   
    blocks -= layer # aumentar la altura
  
    height += 1 # pasar a la siguiente capa
  
    layer += 1


print("La altura de la pirámide:", height)
