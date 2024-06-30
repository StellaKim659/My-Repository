#!pip install yfinance==0.1.70
#!pip install pandas==2.2.2
#!pip install nbformat
#!pip install pandas


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Question 1: Use yfinance to Extract Stock Data
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period='max')
tesla_data.reset_index(inplace=True)
tesla_data.head()

# Question 2: Use Webscraping to Extract Tesla Revenue Data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
tesla_data  = requests.get(url).text
print(tesla_data)
tables = pd.read_html(url)
tesla_revenue = tables[1]
tesla_revenue.columns = ['Date', 'Revenue']
print(tesla_revenue)
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace('$', '').str.replace(',', '')
print(tesla_revenue)
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
print(tesla_revenue.tail(5))

# Question 3: Use yfinance to Extract Stock Data
GameStop = yf.Ticker("GME")
gme_data = GameStop.history(period='max')
gme_data.reset_index(inplace=True)
gme_data.head()

# Question 4: Use Webscraping to Extract GME Revenue Data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
gme_data  = requests.get(url).text
tables = pd.read_html(url)
gme_revenue = tables[1]
gme_revenue.columns = ['Date', 'Revenue']
print(gme_revenue)
gme_revenue['Revenue'] = gme_revenue['Revenue'].str.replace('$', '').str.replace(',', '')
print(gme_revenue)
print(gme_revenue.tail(5))


# Question 5 : Plot Tesla Stock Graph
def make_graph(tesla_data, tesla_revenue, 'Tesla'):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = 0.3)
    tesla_data_specific = tesla_data[tesla_data.Date <= '2021-06-30']
    tesla_revenue_specific = tesla_revenue[tesla_revenue.Date <= '2021-06-30']

    fig.add_trace(go.Scatter(x=pd.to_datetime(tesla_data_specific.Date, infer_datetime_format=True), y=tesla_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(tesla_revenue_specific.Date, infer_datetime_format=True), y=tesla_revenue_specific.Revenue.astype(float), name="Revenue"), row=2, col=1)

    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False, height=900, title='Tesla', xaxis_rangeslider_visible=True)

    fig.show()




# Question 6: Plot GameStop Stock Graph
def make_graph(gme_data, gme_revenue, 'GameStop'):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = 0.3)
    gme_data_specific = gme_data[gme_data.Date <= '2021-06-30']
    gme_revenue_specific = gme_revenue[gme_revenue.Date  <= '2021-06-30']

    fig.add_trace(go.Scatter(x=pd.to_datetime(gme_data_specific.Date, infer_datetime_format=True), y=gme_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(gme_revenue_specific.Date, infer_datetime_format=True), y=gme_revenue_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)

    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False, height=900, title='GameStop', xaxis_rangeslider_visible=True)

    fig.show()