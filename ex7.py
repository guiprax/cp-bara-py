
testes = [
    380,    
    1250,   
    70,    
    15,    
    -100,   
    0,      
]


cedulas = [200, 100, 50, 20, 10]


def validar_saque(valor):
   
    if valor <= 0:
        return False, "Valor inválido: o saque deve ser maior que zero"
    
   
    if valor % 10 != 0:
        return False, "Valor inválido: o saque deve ser múltiplo de 10"
    
    return True, "Válido"


def calcular_cedulas(valor):
   
    quantidade_cedulas = {}
    
   
    for cedula in cedulas:
        quantidade = valor // cedula  # Divisão inteira
        quantidade_cedulas[cedula] = quantidade
        valor -= cedula * quantidade  # Diminui o valor
    
    return quantidade_cedulas


def exibir_saque(valor, cedulas_usadas):
    print("=" * 40)
    print(f"=== Saque: R$ {valor} ===")
    print("=" * 40)
    
    total_cedulas = 0
    
    for cedula in cedulas:
        quantidade = cedulas_usadas[cedula]
        total_cedulas += quantidade
        
       
        if quantidade > 0:
            print(f"R$ {cedula}: {quantidade} cédula(s)")
        else:
            print(f"R$ {cedula}: 0 cédula(s)")
    
    print("=" * 40)
    print(f"Total de cédulas: {total_cedulas}")
    print("=" * 40)
    print()


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
