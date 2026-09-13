import yfinance as yf

def buscar_preco(ticker):
    ativo = yf.Ticker(ticker)
    dados = ativo.history(period="1d")
    preco_atual = dados["Close"].iloc[-1]
    return preco_atual