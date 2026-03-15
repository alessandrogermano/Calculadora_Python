def pegar_nmro():
    while True:
        try:
            numero = float(input("Digite um número: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
historico = []
num1 = pegar_nmro()
while True:
    operacao = input("\nDigite a operação (+, -, *, /, //), 'hist', 'limpar' ou 'sair' para encerrar: ")
    if operacao.lower() == "sair":
        print("Encerrando a calculadora. Até mais!")
        break
    if operacao.lower() == "hist":
        if historico:
            print("\nHistórico:")
            for conta in historico:
                print(conta)
        else:
            print("Nenhuma conta no histórico.")
        continue
    if operacao.lower() == "limpar":
        print("Calculadora reiniciada.")
        historico.clear()
        num1 = pegar_nmro()
        continue
    num2 = pegar_nmro()
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            continue
    elif operacao == "//":
        if num2 != 0:
            resultado = num1 // num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            continue
    else:
        print("Operação inválida.")
        continue
    conta = f"{num1} {operacao} {num2} = {resultado}"
    historico.append(conta)
    print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
    num1 = resultado