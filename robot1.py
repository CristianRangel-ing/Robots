import math

def calcular_volumen_esfera(radio):
    """
    Calcula el volumen de una esfera dado su radio.
    Fórmula: (4/3) * π * r^3

    :param radio: Radio de la esfera (float o int)
    :return: Volumen de la esfera (float)
    """
    if radio <= 0:
        raise ValueError("El radio debe ser un número positivo.")

    volumen = (4/3) * math.pi * math.pow(radio, 3)
    return volumen

if __name__ == "__main__":
    try:
        radio = float(input("Introduce el radio de la esfera: "))
        volumen = calcular_volumen_esfera(radio)
        print(f"El volumen de la esfera con radio {radio} es: {volumen:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
