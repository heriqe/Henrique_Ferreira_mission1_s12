class Conversor_Temperaturas:
    def __init__(self) -> None:
        pass
    def CelsiusParaFahrenheit(celsius):
        return (celsius * 9/5) + 32
    def FahrenheitParaCelsius(Fahrenheit):
        return (Fahrenheit - 32) * 5/9
    print("*Conversor de Temperaturas*")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius")
    while True:
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = CelsiusParaFahrenheit(celsius)
            print(f"{celsius}° Celsius é igual a {fahrenheit}° Fahrenheit")
        elif escolha == "2":
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius = FahrenheitParaCelsius(fahrenheit)
            print(f"{fahrenheit}° Fahrenheit é igual a {celsius}° Celsius")
        elif escolha=="sair":
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")