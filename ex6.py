
testes = [
    (29, 2, 2024),   
    (29, 2, 2023),   
    (31, 4, 2025),   
    (15, 8, 2025),   
    (29, 2, 2000),   
    (29, 2, 1900),   
    (5, 13, 2025),   
    (0, 6, 2025),    
]


meses_dias = {
    1: ("janeiro", 31),
    2: ("fevereiro", 28),
    3: ("março", 31),
    4: ("abril", 30),
    5: ("maio", 31),
    6: ("junho", 30),
    7: ("julho", 31),
    8: ("agosto", 31),
    9: ("setembro", 30),
    10: ("outubro", 31),
    11: ("novembro", 30),
    12: ("dezembro", 31),
}


def eh_bissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False


def obter_dias_mes(mes, ano):
    if mes not in meses_dias:
        return None
    
    nome_mes, dias = meses_dias[mes]
    
   
    if mes == 2 and eh_bissexto(ano):
        return nome_mes, 29
    
    return nome_mes, dias


def validar_data(dia, mes, ano):
    
    if mes < 1 or mes > 12:
        return False, f"Data inválida: mês {mes} não existe (deve ser de 1 a 12)"
    
    
    resultado_mes = obter_dias_mes(mes, ano)
    if resultado_mes is None:
        return False, f"Data inválida: mês {mes} não existe"
    
    nome_mes, dias_mes = resultado_mes
    
   
    if dia < 1 or dia > dias_mes:
        return False, f"Data inválida: {nome_mes} de {ano} tem apenas {dias_mes} dias"
    
    return True, "Data válida!"


for dia, mes, ano in testes:
    bissexto = eh_bissexto(ano)
    status_bissexto = "Sim" if bissexto else "Não"
    
    valida, mensagem = validar_data(dia, mes, ano)
    
    print("=" * 50)
    print(f"Data: {dia:02d}/{mes:02d}/{ano}")
    print(f"Ano bissexto: {status_bissexto}")
    print(mensagem)
    print("=" * 50)
    print()
