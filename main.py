# Lista de idades para testar
idades = [5, 15, 25, 70, -3, 150]

# Função para verificar a categoria de idade
def verificar_idade(idade):
    if idade < 0 or idade > 120:
        return "Idade inválida"
    elif idade >= 0 and idade <= 11:
        return "Criança"
    elif idade >= 12 and idade <= 17:
        return "Adolescente"
    elif idade >= 18 and idade <= 59:
        return "Adulto"
    else:  # idade >= 60 e <= 120
        return "Idoso"

# Testar cada idade
for idade in idades:
    resultado = verificar_idade(idade)
    print(f"Idade {idade}   → {resultado}")