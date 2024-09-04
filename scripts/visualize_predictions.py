import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados de previsões
results = pd.read_csv('results/predictions.csv')

# Criar o gráfico
plt.figure(figsize=(14, 7))
plt.plot(results['Real'], label='Valores Reais', color='blue')
plt.plot(results['Previsão'], label='Previsões', color='red', linestyle='--')
plt.title('Comparação entre Valores Reais e Previsões')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)

# Salvar o gráfico
plt.savefig('results/forecast_comparison.png')
plt.show()
