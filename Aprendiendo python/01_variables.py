# Variables  

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenación de variables en un print

print(my_string_variable, my_int_variable,my_bool_variable) # Tipo 'NoneType'
print("Este es el valor de:", my_bool_variable)

# Funciones del sistema 

print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!

name, surname, alias, age = "Alejandro ", "Rodriguez", "Maniaco", 21
print( "Me llamo:",name,surname,"Mi edad es:",age,"Y mi alias es:",alias)

#inputs

name =input('¿Cual es tu nombre?')
age = input('¿Cuantos años tienes?')
print(name)
print(age)

#Cambiamos su tipo

name = 35
age ='Alejandro'
print(name)
print(age)

#Forzamos el tipo

address: str = "Mi dirección"
address = 32
print(type(address))


