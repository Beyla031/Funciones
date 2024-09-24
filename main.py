from verificador import minusculas, mayusculas, numeros, mas_de_8_caracteres

password = input("Ingresa una contraseña: ")

seguridad = 0

if minusculas(password):
    seguridad += 25

if mayusculas(password):
    seguridad += 25

if numeros(password):
    seguridad += 25

if mas_de_8_caracteres(password):
    seguridad += 25

if seguridad == 100:
    print("La contraseña es 100% segura.")
elif seguridad == 75:
    print("La contraseña es 75% segura.")
elif seguridad == 50:
    print("La contraseña es 50% segura.")
elif seguridad == 25:
    print("La contraseña es 25% segura.")
else:
    print("La contraseña no es segura.")
