import riskfolio as rp
import yfinance as yf
import matplotlib.pyplot as plt

assets = [
    "PANW", #Palo Alto Networks 
    "NVDA", #Nvidia
    "AAPL", #Apple
    "MSFT", #Microsoft
    "GOOG", #Alphabet (google)
    "TSLA", #Tesla
    "DIS",  #Disney
    "AXP",  #American Express
    "GLD",  #Gold
    "STX",  #Seagate
    "WDC",  #Western Digital
    "MADE", #US manufacturing sector
    "^GSPC",#S&P 500
]

data = yf.download(
    assets,
    start="2018-01-01",
    end="2024-08-08",
)
data = data["Close"]

returns = data.pct_change().dropna()

returns.median().sort_values(ascending=False).to_frame(name="median_return")

rp.plot_clusters(
    returns= returns, 
    codependence= 'pearson',
    linkage= 'ward',
    k= None,
    max_k= 13,
    leaf_order= True,
    dendrogram= True,
    ax= None
)

plt.show()

print("done!")