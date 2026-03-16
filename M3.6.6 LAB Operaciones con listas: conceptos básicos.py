my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unique_numbers = []

# Recorrer la lista original
for number in my_list:
    # Si el número no está en la lista única, lo agregamos
    if number not in unique_numbers:
        unique_numbers.append(number)

print("La lista con elementos únicos:")
print(unique_numbers)
