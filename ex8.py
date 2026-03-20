# Lista de testes com cenários de estacionamento
testes = [
    {"entrada": 14, "saida": 16, "placa_final": 3, "dia": "quarta"},
    # 2 horas: R$10 + R$5 = R$15.00

    {"entrada": 9,  "saida": 9,  "placa_final": 7, "dia": "sexta"},
    # Menos de 1 hora: R$10.00 (mínimo)

    {"entrada": 23, "saida": 2,  "placa_final": 5, "dia": "sabado"},
    # 3 horas noturnas: (R$10 + R$5 + R$5) * 1.50 = R$30.00

    {"entrada": 8,  "saida": 12, "placa_final": 4, "dia": "segunda"},
    # 4 horas: R$10 + R$5 + R$5 + R$5 = R$25.00, desconto 10% = R$22.50

    {"entrada": 20, "saida": 3,  "placa_final": 2, "dia": "segunda"},
    # 7 horas, noturno + desconto segunda placa par
]

# Função para calcular horas de permanência
def calcular_horas(entrada, saida):
    if saida > entrada:
        # Mesmo dia
        horas = saida - entrada
    else:
        # Passou da meia-noite
        horas = (24 - entrada) + saida
    
    # Se ficou menos de 1 hora, cobra 1 hora
    if horas == 0:
        horas = 1
    
    return horas

# Função para calcular tarifa base
def calcular_tarifa_base(horas):
    if horas == 1:
        return 10.00
    else:
        # Primeira hora + horas adicionais
        return 10.00 + (horas - 1) * 5.00

# Função para verificar se tem período noturno
def tem_periodo_noturno(entrada, saida):
    if saida > entrada:
        # Mesmo dia - verifica se está entre 22h e 6h
        return (entrada < 6 and saida > 22) or (entrada >= 22) or (saida <= 6)
    else:
        # Passou da meia-noite - sempre tem noturno
        return True

# Função para calcular desconto de segunda-feira com placa par
def tem_desconto_segunda(placa_final, dia):
    return dia.lower() == "segunda" and placa_final % 2 == 0

# Função para calcular valor final do estacionamento
def calcular_estacionamento(entrada, saida, placa_final, dia):
    # Calcular horas
    horas = calcular_horas(entrada, saida)
    
    # Calcular tarifa base
    tarifa_base = calcular_tarifa_base(horas)
    
    # Verificar período noturno
    noturno = tem_periodo_noturno(entrada, saida)
    adicional_noturno = 0
    
    if noturno:
        adicional_noturno = tarifa_base * 0.50
    
    # Subtotal antes do desconto
    subtotal = tarifa_base + adicional_noturno
    
    # Verificar desconto segunda-feira
    desconto = 0
    if tem_desconto_segunda(placa_final, dia):
        desconto = subtotal * 0.10
    
    # Total final
    total = subtotal - desconto
    
    return {
        "horas": horas,
        "tarifa_base": tarifa_base,
        "adicional_noturno": adicional_noturno,
        "noturno": noturno,
        "subtotal": subtotal,
        "desconto": desconto,
        "total": total
    }

# Função para exibir resultado
def exibir_resultado(entrada, saida, placa_final, dia, resultado):
    print("=" * 50)
    print("       === ESTACIONAMENTO ===")
    print("=" * 50)
    print(f"Entrada: {entrada:02d}h | Saída: {saida:02d}h")
    print(f"Dia da semana: {dia.capitalize()}")
    print(f"Placa final: {placa_final}")
    print(f"Permanência: {resultado['horas']} hora(s)")
    print("-" * 50)
    print(f"Tarifa base:            R$ {resultado['tarifa_base']:.2f}")
    
    if resultado['noturno']:
        print(f"Adicional noturno (50%): R$ {resultado['adicional_noturno']:.2f}")
    
    print(f"Subtotal:               R$ {resultado['subtotal']:.2f}")
    
    if resultado['desconto'] > 0:
        print(f"Desconto 2ª feira (-10%): -R$ {resultado['desconto']:.2f}")
    
    print("-" * 50)
    print(f"TOTAL:                  R$ {resultado['total']:.2f}")
    print("=" * 50)
    print()

# Testar cada cenário
for cenario in testes:
    entrada = cenario["entrada"]
    saida = cenario["saida"]
    placa_final = cenario["placa_final"]
    dia = cenario["dia"]
    
    resultado = calcular_estacionamento(entrada, saida, placa_final, dia)
    exibir_resultado(entrada, saida, placa_final, dia, resultado)