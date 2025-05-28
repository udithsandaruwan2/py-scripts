import yfinance as yf

# Download historical SOL-USD data
df = yf.download("SOL-USD", start="2021-01-01", end="2024-12-31", interval='1d')
df.dropna(inplace=True)
df.reset_index(inplace=True)
