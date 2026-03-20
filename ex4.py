# Lista de testes com os 3 lados do triângulo
testes = [
    (5, 5, 5),    # Equilátero
    (5, 5, 3),    # Isósceles
    (3, 4, 5),    # Escaleno
    (1, 2, 10),   # Não forma triângulo (1 + 2 < 10)
    (0, 5, 5),    # Não forma triângulo (lado zero)
    (7, 7, 12),   # Isósceles
]

# Função para verificar se é um triângulo válido
def eh_triangulo_valido(a, b, c):
    # Todos os lados devem ser maiores que zero
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # A soma de dois lados deve ser maior que o terceiro (testa as 3 combinações)
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

# Função para classificar o triângulo
def classificar_triangulo(a, b, c):
    if not eh_triangulo_valido(a, b, c):
        return "Não forma triângulo"
    
    # Verifica se é equilátero (3 lados iguais)
    if a == b == c:
        return "Equilátero"
    
    # Verifica se é isósceles (2 lados iguais)
    elif a == b or b == c or a == c:
        return "Isósceles"
    
    # Senão é escaleno (3 lados diferentes)
    else:
        return "Escaleno"

# Testar cada combinação de lados
for lado1, lado2, lado3 in testes:
    classificacao = classificar_triangulo(lado1, lado2, lado3)
    print(f"Lados: {lado1}, {lado2}, {lado3}")
    print(f"Triângulo válido: {classificacao}")
    print()  # Linha em branco para melhor leitura