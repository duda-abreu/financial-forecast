# Previsão de Tendências do Mercado Financeiro

## Descrição
Este projeto tem como objetivo prever tendências do mercado financeiro utilizando dados históricos de preços de ações e uma rede neural LSTM (Long Short-Term Memory). O projeto foca em ações do Ibovespa e compara o desempenho com o CDI.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **TensorFlow/Keras**: Para construção e treinamento do modelo LSTM.
- **Yahoo Finance API (via `yfinance`)**: Para obter dados históricos de ações.
- **Pandas**: Manipulação e análise de dados.
- **NumPy**: Cálculos numéricos.
- **Matplotlib**: Visualização de dados.

## Estrutura do Projeto
- **data/**: Diretório para arquivos de dados brutos.
- **models/**: Diretório para salvar e carregar modelos treinados.
- **scripts/**: Scripts para análise e treinamento do modelo.
- **README.md**: Este arquivo.

## Requisitos
- **Python**: 3.8 ou superior
- **Bibliotecas**: `yfinance`, `matplotlib`, `pandas`, `numpy`, `tensorflow`, `keras`

## Como Usar
1. **Clonar o Repositório:**
   git clone https://github.com/duda-abreu/financial-forecast.git
   cd financial-forecast

2. **Criar e ativar o ambiente virtual**
python -m venv .venv
# No Windows:
.venv\Scripts\activate
# No macOS/Linux:
source .venv/bin/activate

3. **Instalar Pacotes Necessários:**
pip install -r requirements.txt

4. **Executar Análise das Ações:**
python scripts/analyze_stocks.py 

O usuário pode inserir o preço atual da ação no momento da análise. O sistema retornará uma recomendação sobre se é um bom momento para comprar, com base no preço médio e teto calculados, e incluirá uma comparação entre o rendimento das ações e o CDI.

5. **Treinar o Modelo:**
python scripts/train_model.py

6. **Avaliar o Modelo e Fazer Previsões:**
python scripts/evaluate_model.py

## Explicação das Ações
O projeto inclui análise das seguintes ações do Ibovespa:
ITUB3: Itaú Unibanco - Setor Financeiro
SANB11: Banco Santander - Setor Financeiro
PETR4: Petrobras - Setor de Energia
VALE3: Vale - Setor de Mineração
BBDC4: Banco Bradesco - Setor Financeiro
BBAS3: Banco do Brasil - Setor Financeiro
ABEV3: Ambev - Setor de Bebidas
BBSE3: BB Seguridade - Setor de Seguros
TAEE11: Taesa - Setor de Energia

## Sobre o CDI
O CDI (Certificado de Depósito Interbancário) é uma taxa de referência para investimentos no Brasil. O projeto compara o desempenho das ações com o CDI para fornecer uma perspectiva sobre a rentabilidade.

## Estratégia de Investimento
A estratégia utilizada neste projeto é baseada na acumulação de ações, com uma meta de possuir 100 ações de cada empresa. O objetivo é acumular essas ações sem a intenção de vendê-las, visando o ganho a longo prazo por meio da distribuição de dividendos.

### Filosofia de Acumulação
- **Não Vendemos Ações**: Escolhemos empresas que apresentam estabilidade e não mudam muito de valor ao longo do tempo. Dessa forma, nosso foco é ser parceiros dessas empresas, beneficiando-se dos dividendos ao invés de buscar ganhos com a valorização e venda das ações.
- **Preço Médio e Preço Teto**: 
- **Preço Médio**: É a média dos preços pagos por uma ação ao longo do tempo. Ajuda a avaliar se o momento atual é vantajoso para comprar mais ações.
- **Preço Teto**: É o limite que estamos dispostos a pagar por uma ação, definido como um valor percentual acima do preço médio. Se o preço atual estiver abaixo do preço teto, consideramos um bom momento para comprar.

### Diversificação de Carteira
A diversificação é essencial para minimizar riscos. Investimos em diferentes setores, limitando o número de ativos conforme o patrimônio disponível. Por exemplo:
- Com um patrimônio de R$50 mil, limitamos nossa carteira a 5 ativos, escolhendo empresas de setores diferentes.

## Comparação com CDI
Para fornecer uma perspectiva mais clara sobre o desempenho das ações, comparamos o rendimento das ações analisadas com o rendimento de 100% do CDI (Certificado de Depósito Interbancário), que é um índice de referência para investimentos de renda fixa no Brasil.

## Rentabilidade e Inflação
A rentabilidade das ações será corrigida pela inflação para garantir que os ganhos reais sejam adequadamente avaliados. Optamos por não investir em FIIs (Fundos de Investimento Imobiliário), pois o nosso foco é exclusivamente em ações de empresas sólidas.

## Observações
Erro de List Index: Se você encontrar um erro relacionado ao índice da lista, verifique se o número selecionado para a ação está dentro do intervalo válido.
Problemas de Codificação: Certifique-se de que o arquivo está salvo com a codificação UTF-8 para evitar problemas de caracteres.