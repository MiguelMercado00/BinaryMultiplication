# Multiplicación binaria
# Por Miguel Ángel Mercado Mercado
# Fecha: 31 de enero de 2024

def multiplicar_binarios(a, b):
    resultado = 0
    multiplicador = 1

    # Mientras b sea mayor a 0
    while b > 0:
        digito_b = b % 10

    # Si el dígito es 1, se suma a resultado el valor de a multiplicado por el multiplicador
        if digito_b == 1:
            resultado = sumar_binarios(resultado, a * multiplicador)

        # Se multiplica el multiplicador por 10 y se divide b entre 10
        multiplicador *= 10
        b //= 10

    return resultado

def sumar_binarios(a, b):
    # Se inicializan las variables
    acarreo = 0
    resultado = 0
    posición = 1

    # Mientras a o b sean mayores a 0 o haya acarreo
    while a > 0 or b > 0 or acarreo > 0:
        digito_a = a % 10
        digito_b = b % 10

    # Se suman los dígitos y el acarreo
        suma = digito_a + digito_b + acarreo
        nuevo_digito = suma % 2
        acarreo = suma // 2

    # Se suma el nuevo dígito al resultado
        resultado += nuevo_digito * posición
        posición *= 10

    # Se divide a y b entre 10
        a //= 10
        b //= 10

    return resultado


def main() :
    x = int(input("Ingrese un número: "))
    y = int(input("Ingrese otro número: "))
    print("El producto de", x, "y", y, "es", multiplicar_binarios(x, y))

main()