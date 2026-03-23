
testes = [
    {"entrada": 14, "saida": 16, "placa_final": 3, "dia": "quarta"},
   

    {"entrada": 9,  "saida": 9,  "placa_final": 7, "dia": "sexta"},
  

    {"entrada": 23, "saida": 2,  "placa_final": 5, "dia": "sabado"},
    

    {"entrada": 8,  "saida": 12, "placa_final": 4, "dia": "segunda"},
   
    {"entrada": 20, "saida": 3,  "placa_final": 2, "dia": "segunda"},
]


def calcular_horas(entrada, saida):
    if saida > entrada:
       
        horas = saida - entrada
    else:
       
        horas = (24 - entrada) + saida
    
   
    if horas == 0:
        horas = 1
    
    return horas


def calcular_tarifa_base(horas):
    if horas == 1:
        return 10.00
    else:
        return 10.00 + (horas - 1) * 5.00


def tem_periodo_noturno(entrada, saida):
    if saida > entrada:
        return (entrada < 6 and saida > 22) or (entrada >= 22) or (saida <= 6)
    else:
        return True
        
def tem_desconto_segunda(placa_final, dia):
    return dia.lower() == "segunda" and placa_final % 2 == 0

def calcular_estacionamento(entrada, saida, placa_final, dia):
    horas = calcular_horas(entrada, saida)
    
  
    tarifa_base = calcular_tarifa_base(horas)
    
  
    noturno = tem_periodo_noturno(entrada, saida)
    adicional_noturno = 0
    
    if noturno:
        adicional_noturno = tarifa_base * 0.50
    
    subtotal = tarifa_base + adicional_noturno
    
    desconto = 0
    if tem_desconto_segunda(placa_final, dia):
        desconto = subtotal * 0.10
    

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

for cenario in testes:
    entrada = cenario["entrada"]
    saida = cenario["saida"]
    placa_final = cenario["placa_final"]
    dia = cenario["dia"]
    
    resultado = calcular_estacionamento(entrada, saida, placa_final, dia)
    exibir_resultado(entrada, saida, placa_final, dia, resultado)
