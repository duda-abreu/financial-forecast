import yfinance as yf
import matplotlib.pyplot as plt

# Lista de ações principais do Ibovespa
ibovespa_stocks = ["ITUB3.SA", "SANB11.SA", "PETR4.SA", "VALE3.SA", "BBDC4.SA", "BBAS3.SA", "ABEV3.SA", "BBSE3.SA", "TAEE11.SA"]

# Taxa CDI (100% CDI)
CDI_ANNUAL_RATE = 0.1120  # Exemplo de 11,20% ao ano

def calculate_cdi_return(period_years):
    return (1 + CDI_ANNUAL_RATE) ** period_years - 1

def analyze_stock(stock):
    print(f"Analisando {stock}...")
    data = yf.download(stock, start="2020-01-01", end="2024-12-31")
    
    if data.empty:
        print(f"Não foram encontrados dados para {stock}.")
        return
    
    # Preço obtido pela API
    current_price_api = data['Close'].iloc[-1]
    
    # Solicitar ao usuário o preço atual
    try:
        current_price_user = float(input(f"Insira o preço atual da ação {stock}: R$"))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return

    average_price = data['Close'].mean()
    ceiling_price = average_price * 1.1  # Exemplo: 10% acima do preço médio

    period_years = (data.index[-1] - data.index[0]).days / 365.25
    stock_return = (current_price_api / data['Close'].iloc[0]) - 1
    cdi_return = calculate_cdi_return(period_years)

    print(f"Ação: {stock}")
    print(f"Preço atual (API): R${current_price_api:.2f}")
    print(f"Preço atual informado: R${current_price_user:.2f}")
    print(f"Preço médio: R${average_price:.2f}")
    print(f"Preço teto: R${ceiling_price:.2f}")
    print(f"Retorno da ação (API): {stock_return * 100:.2f}%")
    print(f"Retorno do CDI: {cdi_return * 100:.2f}%")
    
    if stock_return > cdi_return:
        print("A ação foi mais vantajosa que o CDI.")
    else:
        print("O CDI foi mais vantajoso que a ação.")
    
    if current_price_user <= average_price:
        print("É um bom momento para investir.")
    elif current_price_user > ceiling_price:
        print("O preço está acima do teto. Espere uma oportunidade melhor.")
    else:
        print("O preço está acima da média, mas ainda pode ser um bom momento dependendo da estratégia.")
    print("-" * 50)
    
    plot_stock_chart(data, stock)

def plot_stock_chart(data, stock):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Preço de Fechamento')
    plt.axhline(data['Close'].mean(), color='green', linestyle='--', label='Preço Médio')
    plt.axhline(data['Close'].iloc[-1], color='red', linestyle='--', label='Preço Atual Informado')
    plt.title(f"Evolução de preço - {stock}")
    plt.xlabel("Data")
    plt.ylabel("Preço (R$)")
    plt.legend()
    plt.show()

def main():
    print("Escolha uma ação:")
    for i, stock in enumerate(ibovespa_stocks):
        print(f"{i + 1}. {stock}")
    
    try:
        choice = int(input("Digite o número da ação: ")) - 1
        if choice < 0 or choice >= len(ibovespa_stocks):
            raise IndexError
        selected_stock = ibovespa_stocks[choice]
    except (ValueError, IndexError):
        print("Escolha inválida. Por favor, digite um número válido.")
        return
    
    analyze_stock(selected_stock)

if __name__ == "__main__":
    main()

