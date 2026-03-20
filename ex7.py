# Lista de testes com valores de saque
testes = [
    380,    # 1x R$200, 1x R$100, 1x R$50, 1x R$20, 1x R$10
    1250,   # 6x R$200, 0x R$100, 1x R$50, 0x R$20, 0x R$10
    70,     # 0x R$200, 0x R$100, 1x R$50, 1x R$20, 0x R$10
    15,     # Inválido — não é múltiplo de 10
    -100,   # Inválido — valor negativo
    0,      # Inválido — valor zero
]

# Cédulas disponíveis em ordem decrescente
cedulas = [200, 100, 50, 20, 10]

# Função para validar o valor de saque
def validar_saque(valor):
    # Verifica se é positivo
    if valor <= 0:
        return False, "Valor inválido: o saque deve ser maior que zero"
    
    # Verifica se é múltiplo de 10
    if valor % 10 != 0:
        return False, "Valor inválido: o saque deve ser múltiplo de 10"
    
    return True, "Válido"

# Função para calcular as cédulas necessárias
def calcular_cedulas(valor):
    # Dicionário para armazenar quantidade de cada cédula
    quantidade_cedulas = {}
    
    # Percorre cada cédula em ordem decrescente
    for cedula in cedulas:
        quantidade = valor // cedula  # Divisão inteira
        quantidade_cedulas[cedula] = quantidade
        valor -= cedula * quantidade  # Diminui o valor
    
    return quantidade_cedulas

# Função para exibir o resultado do saque
def exibir_saque(valor, cedulas_usadas):
    print("=" * 40)
    print(f"=== Saque: R$ {valor} ===")
    print("=" * 40)
    
    total_cedulas = 0
    
    for cedula in cedulas:
        quantidade = cedulas_usadas[cedula]
        total_cedulas += quantidade
        
        # Formata a saída com alinhamento
        if quantidade > 0:
            print(f"R$ {cedula}: {quantidade} cédula(s)")
        else:
            print(f"R$ {cedula}: 0 cédula(s)")
    
    print("=" * 40)
    print(f"Total de cédulas: {total_cedulas}")
    print("=" * 40)
    print()

# Testar cada valor
for valor in testes:
    valido, mensagem = validar_saque(valor)
    
    if valido:
        cedulas_usadas = calcular_cedulas(valor)
        exibir_saque(valor, cedulas_usadas)
    else:
        print("=" * 40)
        print(f"=== Saque: R$ {valor} ===")
        print("=" * 40)
        print(mensagem)
        print("=" * 40)
        print()