import random

# Opções:
# 1 = Pedra
# 2 = Papel
# 3 = Tesoura
# 4 = Lagarto
# 5 = Spock

# Dicionário com nomes das opções
opcoes = {
    1: "Pedra",
    2: "Papel",
    3: "Tesoura",
    4: "Lagarto",
    5: "Spock"
}

# Tabela de vitórias — quem a chave vence e com qual ação
# Formato: chave vence: [(número_perdedor, ação), ...]
vitoria = {
    1: [(3, "quebra"), (4, "esmaga")],           # Pedra quebra Tesoura, esmaga Lagarto
    2: [(1, "cobre"), (5, "refuta")],            # Papel cobre Pedra, refuta Spock
    3: [(2, "corta"), (4, "decapita")],          # Tesoura corta Papel, decapita Lagarto
    4: [(2, "come"), (5, "envenena")],           # Lagarto come Papel, envenena Spock
    5: [(1, "vaporiza"), (3, "derrete")]         # Spock vaporiza Pedra, derrete Tesoura
}

# Função para validar entrada do jogador
def obter_escolha_jogador():
    while True:
        try:
            escolha = int(input("\nEscolha uma opção:\n[1] Pedra\n[2] Papel\n[3] Tesoura\n[4] Lagarto\n[5] Spock\n\nSua escolha: "))
            
            if escolha < 1 or escolha > 5:
                print(" Opção inválida! Digite um número de 1 a 5.")
                continue
            
            return escolha
        
        except ValueError:
            print(" Erro! Digite um número inteiro.")

# Função para determinar o resultado do jogo
def determinar_resultado(jogador, computador):
    # Empate
    if jogador == computador:
        return "empate", None, None
    
    # Verificar se o jogador vence
    for perdedor, acao in vitoria[jogador]:
        if perdedor == computador:
            return "venceu", computador, acao
    
    # Se não venceu, o computador vence
    for perdedor, acao in vitoria[computador]:
        if perdedor == jogador:
            return "perdeu", jogador, acao
    
    return "empate", None, None

# Função para exibir o resultado do jogo
def exibir_resultado(escolha_jogador, escolha_computador, resultado, derrotado, acao):
    nome_jogador = opcoes[escolha_jogador]
    nome_computador = opcoes[escolha_computador]
    
    print("\n" + "=" * 50)
    print("        === JOGO RPSTLS ===")
    print("=" * 50)
    print(f"Você:       {nome_jogador}")
    print(f"Computador: {nome_computador}")
    print("=" * 50)
    
    if resultado == "empate":
        print(" Empate!")
    elif resultado == "venceu":
        nome_derrotado = opcoes[derrotado]
        print(f" {nome_jogador} {acao} {nome_derrotado} — Você venceu!")
    elif resultado == "perdeu":
        nome_derrotado = opcoes[derrotado]
        nome_vencedor = opcoes[escolha_computador]
        print(f" {nome_vencedor} {acao} {nome_derrotado} — Computador venceu!")
    
    print("=" * 50)

# Função principal do jogo
def jogar():
    print("\n" + "=" * 50)
    print("   BEM-VINDO AO JOGO PEDRA, PAPEL, TESOURA")
    print("         LAGARTO E SPOCK!")
    print("=" * 50)
    
    while True:
        # Obter escolha do jogador
        escolha_jogador = obter_escolha_jogador()
        
        # Computador escolhe aleatoriamente
        escolha_computador = random.randint(1, 5)
        
        # Determinar resultado
        resultado, derrotado, acao = determinar_resultado(escolha_jogador, escolha_computador)
        
        # Exibir resultado
        exibir_resultado(escolha_jogador, escolha_computador, resultado, derrotado, acao)
        
        # Perguntar se quer jogar novamente
        continuar = input("\nDeseja jogar novamente? (sim/nao): ")
        if continuar.lower() != "sim":
            print("\n Obrigado por jogar! Até logo!\n")
            break

# Executar o jogo
if __name__ == "__main__":
    jogar()
