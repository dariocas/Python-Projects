"""Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla cuántos números
primos hay en el rango que va desde cero hasta ese número
incluido, y va a devolverla cantidad de números primos que
encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos."""

'''def contar_primos(num):
    primos = [2]
    iteracion = 3

    if num < 2:
        return 0

    while iteracion <= num:
        print(f"while i = {iteracion}")
        for n in range(3, iteracion, 2):
            print(f"For n{n} i {iteracion}")
            if iteracion % n == 0:
                print(f"if i={iteracion} % n {n}")
                iteracion += 2
                break

        else:
            primos.append(iteracion)
            print(f"Else i = {iteracion} primos {primos} ")
            iteracion += 2

    print(primos)
    return len(primos)'''

def contar_primos(num1):

    lista = [2]

    iteracion = 3

    if num1 < 2:
        return 0

    while iteracion <= num1:

        for n in range(3,iteracion,2):

            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            lista.append(iteracion)
            iteracion += 2
    print(lista)
    return len(lista)

print(contar_primos(50))