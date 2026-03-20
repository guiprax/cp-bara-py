# Lista de testes com valor da compra e status VIP
testes = [
    (80.00,  "nao"),  # Sem desconto, sem VIP
    (200.00, "nao"),  # 10% = R$ 20.00 → R$ 180.00
    (200.00, "sim"),  # 10% + 5% VIP = R$ 30.00 → R$ 170.00
    (450.00, "nao"),  # 15% = R$ 67.50 → R$ 382.50
    (1000.00, "sim"), # 20% + 5% VIP = R$ 250.00 → R$ 750.00
]

# Função para calcular o desconto baseado no valor
def obter_percentual_desconto(valor):
    if valor <= 100:
        return 0
    elif valor <= 300:
        return 10
    elif valor <= 500:
        return 15
    else:
        return 20

# Função para calcular o desconto total
def calcular_desconto(valor, eh_vip):
    # Obter percentual de desconto por faixa
    percentual_desconto = obter_percentual_desconto(valor)
    
    # Calcular valor do desconto normal
    desconto_normal = valor * (percentual_desconto / 100)
    
    # Calcular desconto VIP (5% extra do valor original)
    desconto_vip = 0
    if eh_vip.lower() == "sim":
        desconto_vip = valor * (5 / 100)
    
    # Calconto total e valor final
    desconto_total = desconto_normal + desconto_vip
    valor_final = valor - desconto_total
    
    return {
        "valor_original": valor,
        "percentual_desconto": percentual_desconto,
        "desconto_normal": desconto_normal,
        "desconto_vip": desconto_vip,
        "desconto_total": desconto_total,
        "valor_final": valor_final
    }

# Testar cada combinação de valor e status VIP
for valor, vip in testes:
    resultado = calcular_desconto(valor, vip)
    
    print("=" * 45)
    print("      === Resumo da Compra ===")
    print("=" * 45)
    print(f"Valor original:        R$ {resultado['valor_original']:.2f}")
    
    if resultado['percentual_desconto'] > 0:
        print(f"Desconto ({resultado['percentual_desconto']}%):       R$ {resultado['desconto_normal']:.2f}")
    else:
        print(f"Desconto:              R$ 0.00")
    
    if resultado['desconto_vip'] > 0:
        print(f"Desconto VIP (5%):     R$ {resultado['desconto_vip']:.2f}")
    
    print(f"Valor final:           R$ {resultado['valor_final']:.2f}")
    print("=" * 45)
    print()