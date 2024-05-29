from conversor_medidas import ConversorMedidas
def menu_principal():
    print("\n**Calculadora de Conversão de Unidades**")
    print("1. Converter Comprimento")
    print("3. Sair")
    opcao=input("Digite a opção desejada:  ")
    return opcao
def sair():
    print("O programa está se encerrando")
escolha=menu_principal
if escolha=="3":
    sair()