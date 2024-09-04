import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from data_loader import load_and_preprocess_data
from tensorflow.keras.models import save_model

# Configurações
n_steps = 50
batch_size = 32
epochs = 20

def build_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(0.2))
    model.add(LSTM(50))
    model.add(Dropout(0.2))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Carregar e preparar os dados
X, y = load_and_preprocess_data('data/stock_data.csv', n_steps)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Dividir dados em treino e teste
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Construir e treinar o modelo
model = build_lstm_model((X_train.shape[1], 1))
model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

# Salvar o modelo
model.save('models/lstm_model.keras')
