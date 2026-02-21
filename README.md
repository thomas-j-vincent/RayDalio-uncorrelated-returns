# RayDalio-uncorrelated-returns

In times of uncertainty Ray Dalio argued towards taking returns from uncorrelated sources, to reduce risk, rather than panicking or attempting to time the market. This program creates a dendrogram to represent which of the selected stocks move together.

## Ray Dalio's Holy Grail explanation:

Ray Dalio aimed to reduce a portfolio's exposure to risk whilst keeping its rate of returns by diversifying its assets. He argues against Warren Buffet's belief that one perfect investment means that there is no need for any diversification and instead suggests that with 15-20 well chosen and uncorrelated return streams any risk will be sufficiently distributed so that overall volatility drops. This builds on modern portfolio theory and the benifits of diversification however, adds a slight twist:
- It emphasises uncorrelated assets rather than more assets,
  
- It aims to balance risk, so that each stream contributes to similar risk rather than similar amounts of capital.

According to Dalio, having around 15 uncorrelated assets can result in an 80% percent reduction in volatility.

### How it works

Two assets with a correlation of 1 will move perfectly together. Two uncorrelated returns (or negatively correlated) will oppose each other, cancelling out each other when they fall. This is somewhat like the traditional bonds-stocks mix although the buffer experienced in this falls apart in crises as correlations tend to rise. Dalio allocates capital based on the volitility, a low volatility stream gets more capital whilst a high volatility one gets less, ensuring not one asset dominates risk, even at low capital weight. Alongside this he splits the future into four regimes:
- Growth & rising inflation
- Growth & falling inflation
- Recession & rising inflation
- Recession & deflation

He ensures each of these make money (or atleast don't lose it) to limit losses. 

### Modern adaptation

In 2025 it was reported that Ray Dalio was emphasising gold more, at one point allocating 10-15% of his portfolio to gold, saying it acts as a shield amongst fiscal stress such as overwhelming debt. He also recommends adjusting dynamically, to allow shifts based on market signals (but still avoiding overtrading)

## The code:

The first few lines are used to import the required modules, these are as follows:

- riskfolio; a library built on top of CVXPY that is made for visualising portfolio optimisations

- yfinance; a library that uses yahoo finance's API's to download market data

- matplotlib; a library that can graph data we have discovered

We then define assets, a requirement for the yfinance library that tells it what stocks/ETFs/commodities to download the data for, these are marked for what the ticker is. (there should always be around 5 assets)
Length is found by measuring the length of the assets list, and converting it into an integer

We then define the data, using the assets list as well as the range of data we want to download and in the line below state that we only want the close prices to be downloaded, this helps ensure prices are steady.
Returns uses the downloaded data to calculate the percentage returns, had we not specified that we only want the close data it would do this for all open, high, low, volume prices - which would be pointless because a portfolio return doesn't care about the high price of the day, only the eventaul price. `.dropna()` ensures that for the first value the percentage change is not calculated, as it would cause an error because there is no previous data to calculate the percentage change from. 
The next line returns the median of all the data, sorts them from high to low - and then puts them in a pandas dataframe called median_return. This dataframe contains the asset ticker in one column and their percentage change in another. Using a dataframe in this situation is benificial as it lets us work with more structured data that we otherwise would not be able to.
`rp.plot_clusters` creates the initial dendrogram of the data, it ensures:
- returns are the returns in the dataframe
- codependence uses the [pearson correlation](#pearson-correlation), where assets that move together are grouped
- linkage uses the [ward methods](#Ward-linkage-method), which minimised variation
- K=None ensures that a set number of groups are not forced and instead the algorithm can calculate it itself
- max_k=length-1, sets a maximum number of groups at the length of the assets(-1 otherwise it wouldn't have to group any), as we only have that amount of assets
- leaf_order groups similar assets so they can be interpreted more easily.
- dendogram ensures that the whole dendogram is drawn
- ax tells matplotlib not to put the data on an axis and instead creates a new diagram

`plt.show()` shows this created graph.

the last line shows that the program should've been completed by printing done in the terminal.


-Thomas

## pearson correlation

Measures linear correlation between sets of data, it is a ratio of the joint variability of two variables, positive when two variables show similar behaviour and negative when they do not (covariance). It is essentially a normalised measurement of covariance so that the value is always between -1 and 1.

## Ward linkage method

Used in hierarchial cluster analysis, Wards method is a special case where choosing the pair of clusters to merge is based on the optimal value of the function, the two tickers that result in the smallest increase in total cluster variance. Where low variance means points are very similar and high variance means that the points are spread out. (it groups similar stocks)

## References:
https://www.investorsjournal.org/post/holy-grail-dalio
https://statoasis.com/post/the-holy-grail-by-ray-dalio
https://www.idnfinancials.com/news/54197/ray-dalio-use-the-holy-grail-strategy-in-times-of-uncertainty%EF%BF%BC
https://www.reuters.com/business/ray-dalio-suggests-gold-shield-us-markets-risk-heart-attack-2025-09-11/
https://ranaroussi.github.io/yfinance/reference/api/yfinance.download.html
https://riskfolio-lib.readthedocs.io/en/latest/index.html
https://en.wikipedia.org/wiki/Ward%27s_method
https://en.wikipedia.org/wiki/Pearson_correlation_coefficient#
https://en.wikipedia.org/wiki/Covariance

