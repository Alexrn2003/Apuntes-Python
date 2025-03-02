### Strings ###

my_string = "Mi String"
my_other_string = 'Mi Otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\n escapado" #Con doble barra se deshace el salto o la tabulación
print(my_scape_string)

# Formateo


name,surname, age ="Alejandro", "Rodríguez", 21

print("Mi nombre es  {} {} y mi edad es {} ".format(name,surname,age))
print("Mi nombre es  %s %s y mi edad es %s " %(name,surname,age))
print(f"Mi nombre es  {name} {surname} y mi edad es {age} ")

#Desempaquetado de caracteres

language = "python"
a,b,c,d,e,f = language
print(a)
print(b)

#División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[1:2:4]
print(language_slice)

#Reverse

revese_language = language[::-1]
print(revese_language)

#Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))
