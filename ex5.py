testes = [
    (80.00,  "nao"),  
    (200.00, "nao"),  
    (200.00, "sim"),  
    (450.00, "nao"),  
    (1000.00, "sim"), 
]


def obter_percentual_desconto(valor):
    if valor <= 100:
        return 0
    elif valor <= 300:
        return 10
    elif valor <= 500:
        return 15
    else:
        return 20


def calcular_desconto(valor, eh_vip):

    percentual_desconto = obter_percentual_desconto(valor)
    

    desconto_normal = valor * (percentual_desconto / 100)
    
 
    desconto_vip = 0
    if eh_vip.lower() == "sim":
        desconto_vip = valor * (5 / 100)
    
 
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
