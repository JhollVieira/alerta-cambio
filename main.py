import time
from precos import buscar_preco
from alertas import verificar_alerta

pares_disponiveis = {
    "1": {"nome": "Dólar/Real", "ticker": "USDBRL=X"},
    "2": {"nome": "Euro/Real", "ticker": "EURBRL=X"},
    "3": {"nome": "Petrobras", "ticker": "PETR4.SA"},
    "4": {"nome": "Vale", "ticker": "VALE3.SA"},   
}

def configurar_ativos():
    ativos_escolhidos = []

    while True:
        print("\nPares Disponíveis:")
        for numero, info in pares_disponiveis.items():
            print(f"{numero} - {info['nome']}")

        escolha = input("\nDigite o número do par que deseja acompanhar: ")

        if escolha not in pares_disponiveis:
            print("Opção inválida, tente novamente.")
            continue
        
        ticker_escolhido = pares_disponiveis[escolha]["ticker"]

        quer_maximo = input("Deseja definir alerta de valor MÁXIMO? (s/n): ")
        valor_maximo = None
        if quer_maximo.lower() == "s":
            valor_maximo = float(input("Digite o valor máximo: "))

        quer_minimo = input("Deseja definir alerta de valor MÍNIMO? (s/n): ")
        valor_minimo = None
        if quer_minimo.lower() == "s":
            valor_minimo = float(input("Digite o valor mínimo: "))

        ativos_escolhidos.append({
            "ticker": ticker_escolhido,
            "valor_maximo": valor_maximo,
            "valor_minimo": valor_minimo

        })

        continuar = input("\nDeseja adicionar outro ativo? (s/n): ")
        if continuar.lower() != "s":
            break

    return ativos_escolhidos

ativos_monitorados = configurar_ativos()

while True:
    for ativo in ativos_monitorados:
        preco_atual = buscar_preco(ativo["ticker"])
        resultado = verificar_alerta(preco_atual, ativo["valor_maximo"], ativo["valor_minimo"])

        if resultado:
            print(resultado)
        else:
            print(f"{ativo['ticker']}: preço atual {preco_atual}, sem alerta")
            
    print("----")
    time.sleep(30)
