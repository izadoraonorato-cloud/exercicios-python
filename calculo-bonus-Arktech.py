# ================================================
# MÓDULOS DE PROCESSAMENTO (def)
# ================================================
def calcular_bonus (salario):
    """Calcula o bônus padrão de 15% da ArkeTech"""
    return salario * 0.15

# ================================================
# INTERFACE DO SISTEMA
# =================================================
print("=========================================")
print("     RH ARKETECH - BÔNUS INICIAL         ")
print("=========================================")

while True:
    print ("\n--- NOVO REGISTRO - --")

    #O .strip() remove espaços em branco digitados sem querer
    nome = input ("Nome completo (ou digite '0' para sair") : " !

    if nome == '0':
    print ("\n Encerrando o painel de bônus. Bom trabalho!") break
    