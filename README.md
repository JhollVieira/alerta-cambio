# Alerta de Câmbio
Monitor de preços de ativos da B3 e pares de Forex, com alertas configuráveis de valor máximo e mínimo. Projeto criado para praticar Python e mercado financeiro.

## O que o projeto faz
- Busca preços em tempo real de ações da B3 e pares de moedas (Forex)
- Permite configurar alertas de preço máximo e/ou mínimo para cada ativo
- Monitora múltiplos ativos simultaneamente, em loop contínuo
- Interface simples via terminal, com menu interativo

## Sobre este projeto
Este é meu primeiro projeto prático em Python, desenvolvido enquanto estudo programação e aplicação para mercado financeiro e cibersegurança. A ideia foi sair da teoria e construir algo funcional do zero — buscando dados reais, criando lógica de alertas e um menu interativo.

## Tecnologias usadas

- Python 3.14
- [yfinance](https://pypi.org/project/yfinance/) — biblioteca para buscar dados financeiros do Yahoo Finance

## Como rodar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/JhollVieira/alerta-cambio.git
cd alerta-cambio
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o programa:
```bash
python main.py
```

5. Siga o menu interativo para escolher os ativos e configurar os alertas desejados.

## Estrutura do projeto

- `main.py` — arquivo principal, contém o menu interativo e o loop de monitoramento
- `precos.py` — função responsável por buscar o preço atual de um ativo
- `alertas.py` — função responsável por verificar se um preço atingiu os limites definidos

## Próximos passos
- Adicionar notícias relacionadas aos ativos monitorados
- Migrar notificações para Telegram/WhatsApp
- Criar interface gráfica




## Autor
Projeto desenvolvido por [Majestix*Jholl*](https://github.com/JhollVieira)