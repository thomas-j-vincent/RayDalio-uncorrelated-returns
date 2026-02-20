import riskfolio as rp
import pandas as pd
import yfinance as yf
import seaborn as sns
import pyfolio as pf
import matplotlib.pyplot as plt

assets = [
    "PANW",
    "NVDA",
    "AAPL",
    "MSFT",
    "GOOG",
    "TSLA",
    "DIS",
    "AXP",
    "GLD",
    "^GSPC",
]

data = yf.download(
    assets,
    start="2018-01-01",
    end="2024-08-08",
    progress=False,
    auto_adjust=True,
)
data = data["Close"]
data

returns = data.pct_change().dropna()
returns

returns.median().sort_values(ascending=False).to_frame(name="median_return")

rp.plot_clusters(
    returns= returns, 
    codependence= 'pearson',
    linkage= 'ward',
    k= None,
    max_k= 10,
    leaf_order= True,
    dendrogram= True,
    ax= None
)

plt.show()

print("done!")