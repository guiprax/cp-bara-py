# Teste com estes cenários
testes = [
    {"salario": 2000.00, "dependentes": 0, "pensao": 0, "idoso": False},
    # INSS: R$ 157.17 | Base: R$ 1.842.83 | IR: isento

    {"salario": 5000.00, "dependentes": 2, "pensao": 0, "idoso": False},
    # INSS: R$ 509.59 | Dedução dep: R$ 379.18 | Base: R$ 4.111.23 | IR: R$ 263.02

    {"salario": 8000.00, "dependentes": 1, "pensao": 500, "idoso": False},
    # INSS: R$ 872.77 | Dedução dep: R$ 189.59 | Pensão: R$ 500 | Base: R$ 6.437.64

    {"salario": 3500.00, "dependentes": 0, "pensao": 0, "idoso": True},
    # INSS: R$ 401.36 | Isenção idoso: R$ 1.903.98 | Base: R$ 1.194.66 | IR: isento
]

# Tabela INSS 2025 (faixas)
tabela_inss = [
    (1518.00, 0.075),
    (2793.88, 0.09),
    (4190.83, 0.12),
    (8157.41, 0.14),
    (float('inf'), 0)  # Acima disso é teto
]

# Tabela IR 2025 (faixas)
tabela_ir = [
    (2259.20, 0.00),
    (2826.65, 0.075),
    (3751.05, 0.15),
    (4664.68, 0.225),
    (float('inf'), 0.275)
]

# Função para calcular INSS progressivo
def calcular_inss(salario):
    inss_por_faixa = []
    inss_total = 0
    limite_anterior = 0
    
    for limite, aliquota in tabela_inss:
        if salario <= limite_anterior:
            break
        
        # Determinar o valor a ser tributado nesta faixa
        valor_faixa = min(salario, limite) - limite_anterior
        desconto_faixa = valor_faixa * aliquota
        
        inss_por_faixa.append({
            "limite": limite,
            "aliquota": aliquota,
            "valor_faixa": valor_faixa,
            "desconto": desconto_faixa
        })
        
        inss_total += desconto_faixa
        limite_anterior = limite
    
    return inss_total, inss_por_faixa

# Função para calcular IR progressivo
def calcular_ir(base_calculo):
    ir_por_faixa = []
    ir_total = 0
    limite_anterior = 0
    
    for limite, aliquota in tabela_ir:
        if base_calculo <= limite_anterior:
            break
        
        # Determinar o valor a ser tributado nesta faixa
        valor_faixa = min(base_calculo, limite) - limite_anterior
        desconto_faixa = valor_faixa * aliquota
        
        ir_por_faixa.append({
            "limite": limite,
            "aliquota": aliquota,
            "valor_faixa": valor_faixa,
            "desconto": desconto_faixa
        })
        
        ir_total += desconto_faixa
        limite_anterior = limite
    
    return ir_total, ir_por_faixa

# Função para calcular imposto de renda completo
def calcular_imposto_renda(salario, dependentes, pensao, idoso):
    # Etapa 1: Calcular INSS
    inss_total, inss_por_faixa = calcular_inss(salario)
    
    # Etapa 1: Calcular deduções
    deducao_dependentes = dependentes * 189.59
    deducao_idoso = 1903.98 if idoso else 0
    
    # Etapa 1: Calcular base de cálculo do IR
    base_calculo = salario - inss_total - deducao_dependentes - pensao - deducao_idoso
    base_calculo = max(base_calculo, 0)  # Não pode ser negativa
    
    # Etapa 3: Calcular IR
    ir_total, ir_por_faixa = calcular_ir(base_calculo)
    
    # Calcular salário líquido
    salario_liquido = salario - inss_total - deducao_dependentes - pensao - deducao_idoso - ir_total
    
    return {
        "salario": salario,
        "inss_total": inss_total,
        "inss_por_faixa": inss_por_faixa,
        "deducao_dependentes": deducao_dependentes,
        "pensao": pensao,
        "deducao_idoso": deducao_idoso,
        "base_calculo": base_calculo,
        "ir_total": ir_total,
        "ir_por_faixa": ir_por_faixa,
        "salario_liquido": salario_liquido
    }

# Função para exibir o resultado formatado
def exibir_contracheque(salario, dependentes, pensao, idoso, resultado):
    print("=" * 50)
    print("   CONTRACHEQUE — Cálculo de IR Mensal")
    print("=" * 50)
    print(f"Salário bruto:       R$ {resultado['salario']:,.2f}")
    print()
    
    # INSS detalhado
    print(f"(-) INSS:            R$ {resultado['inss_total']:,.2f}")
    for i, faixa in enumerate(resultado['inss_por_faixa'], 1):
        if faixa['desconto'] > 0:
            aliquota_pct = faixa['aliquota'] * 100
            print(f"    Faixa {aliquota_pct:.1f}%:     R$ {faixa['desconto']:,.2f}")
    print()
    
    # Deduções
    print(f"(-) Dependentes ({dependentes}): R$ {resultado['deducao_dependentes']:,.2f}")
    print(f"(-) Pensão:          R$ {resultado['pensao']:,.2f}")
    print(f"(-) Isenção 65+:     R$ {resultado['deducao_idoso']:,.2f}")
    print()
    
    # Base de cálculo
    print(f"Base de cálculo IR:  R$ {resultado['base_calculo']:,.2f}")
    print()
    
    # IR detalhado
    print(f"(-) IR:              R$ {resultado['ir_total']:,.2f}")
    for faixa in resultado['ir_por_faixa']:
        if faixa['desconto'] > 0 or faixa['aliquota'] == 0.00:
            aliquota_pct = faixa['aliquota'] * 100
            if aliquota_pct == 0:
                print(f"    Faixa isenta:    R$ {faixa['desconto']:,.2f}")
            else:
                print(f"    Faixa {aliquota_pct:.1f}%:      R$ {faixa['desconto']:,.2f}")
    print()
    
    # Resultado final
    print("=" * 50)
    print(f"Salário líquido:     R$ {resultado['salario_liquido']:,.2f}")
    print("=" * 50)
    print()

# Executar testes
for i, teste in enumerate(testes, 1):
    print(f"\n{'#' * 50}")
    print(f"# CENÁRIO {i}")
    print(f"{'#' * 50}")
    
    resultado = calcular_imposto_renda(
        teste["salario"],
        teste["dependentes"],
        teste["pensao"],
        teste["idoso"]
    )
    
    exibir_contracheque(
        teste["salario"],
        teste["dependentes"],
        teste["pensao"],
        teste["idoso"],
        resultado
    )