testes = [
    (5, 5, 5),    # Equilátero
    (5, 5, 3),    # Isósceles
    (3, 4, 5),    # Escaleno
    (1, 2, 10),   # Não forma triângulo (1 + 2 < 10)
    (0, 5, 5),    # Não forma triângulo (lado zero)
    (7, 7, 12),   # Isósceles
]

def eh_triangulo_valido(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return False
    

    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False


def classificar_triangulo(a, b, c):
    if not eh_triangulo_valido(a, b, c):
        return "Não forma triângulo"
    

    if a == b == c:
        return "Equilátero"
    
 
    elif a == b or b == c or a == c:
        return "Isósceles"
    

    else:
        return "Escaleno"


for lado1, lado2, lado3 in testes:
    classificacao = classificar_triangulo(lado1, lado2, lado3)
    print(f"Lados: {lado1}, {lado2}, {lado3}")
    print(f"Triângulo válido: {classificacao}")
    print() 
