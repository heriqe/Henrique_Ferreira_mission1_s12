def sair():
    print("Encerrando o programa...")

def menu_principal():
    while True:
        print("\n*Calculadora de Conversão de Unidades*")
        print("1. Conversor de Medidas")
        print("2. Conversor de Temperaturas")   
        print("3. Sair")
        opção = input("Digite a opção desejada: ")
        if opção == "1":
            from conversor_medidas import ConversorMedidas
        elif opção == "2":
            from conversor_temperaturas import Conversor_Temperaturas
        elif opção == "3":
            sair()
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()
