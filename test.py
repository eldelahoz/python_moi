email = input("Introduce una direccion de email: ")


def repetir_email():
    pass


while email.find("@") == 0:
    print("No puedes poner la @ al inicio")
    print("Tienes que ingresarla corectamente".center(50))
    email = input("Introduce una direccion de email:")
while email.find("@") == len(email) - 1:
    print("No se puede poner la @ a lo ultimo")
    print("Tienes que ingresarla corectamente".center(50))
    email = input("Introduce una direccion de email:")
while not "@" in email.lower():
    print("No hay @ en tu direccion de email")
    print("Tienes que ingresarla corectamente".center(50))
    email = input("Introduce una direccion de email:")
while email.count("@") != 1:
    print("Hay mas de una @")
    print("Tienes que ingresarla corectamente".center(50))
    email = input("Introduce una direccion de email:")

print("Tu direccion es corecta: {}".format(email))
