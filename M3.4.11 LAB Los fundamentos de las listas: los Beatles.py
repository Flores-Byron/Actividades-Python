# paso 1: crea la lista llamada beatles
beatles = []
print("Paso 1:", beatles)

# paso 2: agrega los integrantes
beatles.append("John lenon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3: ingresa a los miembros que faltan
for i in range(2):
    nombre=input("Ingresa los miembros que faltan:")
    beatles.append(nombre)
print("Paso 3:", beatles)

# paso 4: elimina a Stu Sutcliffe y Pete Best de la lista
del beatles[3]
del beatles[3]
print("Lista después de eliminar miembros:", beatles)
print("Paso 4:", beatles)

# paso 5inserta a Ringo star al principio de la lista
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))

