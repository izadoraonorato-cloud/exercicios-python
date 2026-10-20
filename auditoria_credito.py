# Arquivo: Credito_ArkeTech_NomeDaDupla.py
# Descrição: Sistema automatizado de triagem de crédito para a ArkeTech.
# Aluno / Copiloto: [izadora beatriz onorato]

def auditoria_credito():
    print("=" * 54)
    print("       SISTEMA DE AUDITORIA DE CRÉDITO - ARKETECH       ")
    print("=" * 54)
    
    # 1. Coleta de dados de entrada
    nome_empresa = input("Digite o nome da empresa solicitante: ").strip()
    
    try:
        faturamento_mensal = float(input("Digite o faturamento mensal (R$): "))
        valor_emprestimo = float(input("Digite o valor total do empréstimo solicitado (R$): "))
    except ValueError:
        print("\n[ERRO] Por favor, insira apenas valores numéricos válidos para faturamento e empréstimo.")
        return

    if faturamento_mensal < 0 or valor_emprestimo < 0:
        print("\n[ERRO] Os valores financeiros não podem ser negativos.")
        return

    # 2. Cálculos parametrizados
    # Simulação da parcela mensal dividida em 12 vezes sem juros
    parcela_mensal = valor_emprestimo / 12
    
    # Cálculo do percentual de comprometimento da renda
    if faturamento_mensal > 0:
        percentual_comprometimento = (parcela_mensal / faturamento_mensal) * 100
    else:
        percentual_comprometimento = 100.0 if valor_emprestimo > 0 else 0.0

    # 3. Árvore de Decisão baseada no risco
    if parcela_mensal <= (faturamento_mensal * 0.30):
        status = "APROVADO"
        descricao = "Risco Baixo. A parcela compromete até 30% do faturamento."
    elif parcela_mensal <= (faturamento_mensal * 0.50):
        status = "EM ANÁLISE (Risco Moderado)"
        descricao = "Risco Moderado. A parcela compromete entre 30,1% e 50% do faturamento."
    else:
        status = "RECUSADO"
        descricao = "Risco Alto. A parcela ultrapassa 50% do faturamento mensal."

    # 4. Saída formatada com f-strings
    print("\n" + "=" * 54)
    print("                  PARECER DE CRÉDITO                  ")
    print("=" * 54)
    print(f"Empresa Solicitante  : {nome_empresa}")
    print(f"Faturamento Mensal   : R$ {faturamento_mensal:,.2f}")
    print(f"Valor do Empréstimo  : R$ {valor_emprestimo:,.2f}")
    print(f"Parcela Mensal (12x) : R$ {parcela_mensal:,.2f}")
    print(f"Comprometimento      : {percentual_comprometimento:.2f}% do faturamento")
    print("-" * 54)
    print(f"STATUS DO PARECER    : {status}")
    print(f"Motivo / Detalhes    : {descricao}")
    print("=" * 54)

if __name__ == "__main__":
    auditoria_credito()