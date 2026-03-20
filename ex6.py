# Lista de testes com dia, mês e ano
testes = [
    (29, 2, 2024),   # Válida — 2024 é bissexto
    (29, 2, 2023),   # Inválida — 2023 não é bissexto
    (31, 4, 2025),   # Inválida — abril tem 30 dias
    (15, 8, 2025),   # Válida — 15/08/2025
    (29, 2, 2000),   # Válida — 2000 é bissexto (divisível por 400)
    (29, 2, 1900),   # Inválida — 1900 NÃO é bissexto (divisível por 100)
    (5, 13, 2025),   # Inválida — mês 13 não existe
    (0, 6, 2025),    # Inválida — dia 0 não existe
]

# Meses com seus nomes e dias
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

# Função para verificar se é ano bissexto
def eh_bissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False

# Função para obter dias no mês
def obter_dias_mes(mes, ano):
    if mes not in meses_dias:
        return None
    
    nome_mes, dias = meses_dias[mes]
    
    # Se é fevereiro e o ano é bissexto, tem 29 dias
    if mes == 2 and eh_bissexto(ano):
        return nome_mes, 29
    
    return nome_mes, dias

# Função para validar a data
def validar_data(dia, mes, ano):
    # Validar mês
    if mes < 1 or mes > 12:
        return False, f"Data inválida: mês {mes} não existe (deve ser de 1 a 12)"
    
    # Obter informações do mês
    resultado_mes = obter_dias_mes(mes, ano)
    if resultado_mes is None:
        return False, f"Data inválida: mês {mes} não existe"
    
    nome_mes, dias_mes = resultado_mes
    
    # Validar dia
    if dia < 1 or dia > dias_mes:
        return False, f"Data inválida: {nome_mes} de {ano} tem apenas {dias_mes} dias"
    
    return True, "Data válida!"

# Testar cada data
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