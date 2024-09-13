import json

def calcular_faturamento():
    with open('data/faturamento.json') as file:
        dados = json.load(file)

    faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]
    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_media

if __name__ == "__main__":
    menor, maior, dias_acima_media = calcular_faturamento()
    print(f"Menor valor de faturamento: R${menor:.2f}")
    print(f"Maior valor de faturamento: R${maior:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
