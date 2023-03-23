# Le pedimos al usuario que nos diga una frase o varias
frase = input('Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ')

# Creamos una lista con todas las palabras de la frase (Se separan cada vez que encuentran un espacio)
palabras_separadas = frase.split(' ')

# Usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#En caso de que tarde más de un minuto le decimos que para un poco
if cantidad_de_palabras > 120:
  print("Para flaco tampoco te pedí un testamento")

# Calculamos cuanto tardaría en decir las palabras y se lo decimos
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dalto lo diría en {round(cantidad_de_palabras / 2 * 0.7,1)} segundos')


