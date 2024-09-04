from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
from data_loader import load_and_preprocess_data

# Configurações
n_steps = 50

# Caminho para o arquivo do modelo
model_path = 'models/lstm_model.keras'

# Verificar se o arquivo existe
import os
if not os.path.isfile(model_path):
    raise FileNotFoundError(f"Arquivo não encontrado: {model_path}")

# Carregar o modelo treinado
model = load_model(model_path)

# Carregar e preparar os dados
X, y = load_and_preprocess_data('data/stock_data.csv', n_steps)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Dividir dados em treino e teste
train_size = int(len(X) * 0.8)
X_test = X[train_size:]
y_test = y[train_size:]

# Fazer previsões
predictions = model.predict(X_test)

# Criar DataFrame para previsões e salvar em CSV
results = pd.DataFrame({
    'Real': y_test.flatten(),
    'Previsão': predictions.flatten()
})
results.to_csv('results/predictions.csv', index=False)

print("Previsões salvas em 'results/predictions.csv'.")
