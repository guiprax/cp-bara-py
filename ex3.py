# Cotações fixas para o exercício
cotacoes = {
    "dolar": 5.15,
    "euro": 5.55,
    "libra": 6.45
}

# Função para realizar a conversão
def converter_moeda(valor_reais, moeda):
    if valor_reais < 0:
        return "Valor inválido"
    
    if moeda == 1:
        valor_convertido = valor_reais / cotacoes["dolar"]
        simbolo = "US$"
        return f"R$ {valor_reais:.2f} = {simbolo} {valor_convertido:.2f}"
    
    elif moeda == 2:
        valor_convertido = valor_reais / cotacoes["euro"]
        simbolo = "€"
        return f"R$ {valor_reais:.2f} = {simbolo} {valor_convertido:.2f}"
    
    elif moeda == 3:
        valor_convertido = valor_reais / cotacoes["libra"]
        simbolo = "£"
        return f"R$ {valor_reais:.2f} = {simbolo} {valor_convertido:.2f}"
    
    else:
        return "Opção inválida"

# Menu principal
while True:
    print("=" * 40)
    print("        CONVERSOR DE MOEDAS")
    print("=" * 40)
    print("[1] Real → Dólar")
    print("[2] Real → Euro")
    print("[3] Real → Libra")
    print("[0] Sair")
    print("=" * 40)
    
    try:
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 0:
            print("Até logo!")
            break
        
        if opcao not in [1, 2, 3]:
            print("Opção inválida\n")
            continue
        
        valor = float(input("Digite o valor em reais (R$): "))
        resultado = converter_moeda(valor, opcao)
        print(f"\n{resultado}\n")
        
    except ValueError:
        print("Por favor, digite números válidos!\n")