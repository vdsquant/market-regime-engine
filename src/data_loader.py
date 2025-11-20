import pandas as pd
import yfinance as yf

# LOAD UK "YIELD" DATA VIA GILT ETFs (STABLE APPROACH)

# UK gilt ETFs:
# IGLS = short gilts (0–5Y)
# IGLT = medium gilts (5–10Y)
# GLTL = long gilts (20Y+)

def load_yield_data():
    tickers = ["IGLS.L", "IGLT.L", "GLTL.L"]
    names = ["ShortGilts", "MediumGilts", "LongGilts"]

    df = yf.download(tickers, start="2005-01-01", auto_adjust=False)

    # MultiIndex case (normal for multiple tickers)
    if isinstance(df.columns, pd.MultiIndex):
        df = df["Close"]

    # Rename columns for better clarity
    df.columns = names

    return df.dropna()

# LOAD UK MARKET DATA (FTSE 100)

def load_market_data():
    data = yf.download("^FTSE", start="2005-01-01", auto_adjust=False)

    if isinstance(data.columns, pd.MultiIndex):
        close = data["Close"]["^FTSE"]
    else:
        close = data["Close"]

    return pd.DataFrame({"FTSE": close}).dropna()


'''
1. 
Attempt 1 - Using Yahoo Finance UK Gilt Yield Tickers

I attempted to fetch UK gilt yields via: GB2Y.GB,  GB5Y.GB, GB10Y.GB, ^VFTSE (UK Volatility Index)

But Yahoo Finance has delisted / removed these series.
All requests returned:
    YFTzMissingError
    Ticker not found

Conclusion:
Yahoo Finance does not provide UK sovereign yields anymore.

2.
Attempt — Using FRED (St. Louis Fed) UK Yield Series

I tried using official FRED tickers: IUDMNPY (2Y), IUDMNP5Y (5Y), IUDMNP10Y (10Y)
Using:
pandas_datareader.data.DataReader(..., "fred")

RED response:
    RemoteDataError
    HTTP 404 / 403 Forbidden

This occurred because BoE UK gilt series were moved
FRED now requires stricter access rules/API keys for many datasets
Some series are discontinued / renamed

Conclusion: Direct FRED access for UK yields is no longer reliable.

3. 
Attempt 3 — Direct CSV from Bank of England
I tried pulling CSV data from https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns...

Even after constructing valid URLs, the server responded with:
    HTTPError: 403 Forbidden

This happened because BoE blocks automated requests unless:
User-Agent is spoofed
Session cookies are passed
Browser headers are replicated

Conclusion: BoE web endpoints block scripted data downloads.

4. 
Working Solution — UK Gilt ETFs (Reliable & Stable)
I solved the problem by replacing raw gilt yields with UK gilt ETFs, which trade on the London Stock Exchange and track yield curve movements:

Curve Point             ETF     Ticker
Short Gilts (0 to 5Y)   IGLS	IGLS.L
Medium Gilts (5 to10Y)	IGLT	IGLT.L
Long Gilts (20Y+)	    GLTL	GLTL.L

These are liquid ETFs whose daily price changes closely follow yield movements — perfect for PCA.

Final working PCA yield set:
tickers = ["IGLS.L", "IGLT.L", "GLTL.L"]
names = ["ShortGilts", "MediumGilts", "LongGilts"]

This I got stable dataset from 2005 to present.
'''