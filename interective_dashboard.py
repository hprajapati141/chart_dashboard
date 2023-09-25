import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import yfinance as yf
import mplfinance as mpl
import math

stock_excel=pd.read_excel('chartink_list.xlsx').fillna("")
stock_list=stock_excel['stock(m_cap_1000)'].tolist()
ind_list=stock_excel['industry'].tolist()
industry_excel=pd.read_excel('industry_wise_seg.xlsx','Sheet2')

#ticker = st.sidebar.selectbox("Select Stock Symbol (e.g., AAPL):",["LSIL.NS","CANBK.NS"])
ticker = st.sidebar.selectbox("Select Stock Symbol (e.g., AAPL):",stock_list)
ind= st.sidebar.selectbox("Select industry:",ind_list)
stock = yf.Ticker(ticker+".NS")

col1,col2,col3=st.columns([2,1,2])
with col1:
    st.title(ticker)
## getting fundaments
mcap=round(stock.info['marketCap']/10**10,2)
with col2:
    st.write(f"**Mcap(1000cr)**_{mcap}")
with col3:
    st.write(stock.info['website'])
with col2:
    st.write(stock.info['industry'])
        
    
    

# Fetch historical stock data using yfinance

df = stock.history(period="100d")

# Try to plot the data using mplfinance
try:
    
    fig1, ax = mpl.plot(df, type='candle',style='charles', volume=True, figsize=(20, 10),returnfig=True)
    st.pyplot(fig1)
except Exception as e:
    st.write("Error:", e)
    
#################################################################################################################################
industries={'Abrasives': ['CARBORUNIV', 'GRINDWELL', 'WENDT'],
      'Aerospace & Defence': ['APOLLO',  'BEL',  'DATAPATTNS',  'DREAMFOLKS',  'HAL','MTARTECH'],
       'Commodity Chemicals': ['ALKALI','BEPL','BODALCHEM','CHEMFAB','DCW','DEEPAKNTR','GANESHBE','GOCLCORP','GRAUWEIL','GUJALKALI',
'HSCL','INDIAGLYCO','INDOBORAX','IVP','KHAICHEM','MANORG','NOCIL','OAL','OCCL','POCL','PREMEXPLN','SADHNANIQ',
'SOLARINDS','SRHHYPOLTD','STYRENIX','TNPETRO','TIRUMALCHM']   }

#comps=industries[ind]
comps=industry_excel[ind].tolist()
comps = [item for item in comps if not(pd.isnull(item)) == True]

df1=pd.DataFrame()
for comp in comps:
    df2=yf.download((comp+'.NS'),period='100d',progress=False)
    df2=df2.pct_change()
    df2=df2.fillna(0)
    df1[comp]=df2['Close']
    
df1['avg']=df1.mean(axis=1)
df1['avg_cumsum']=df1['avg'].cumsum()
df1=df1.fillna(0)
#matplotlib chart
# fig2, ax = plt.subplots(figsize=(20, 10))
# ax.plot(df1.index, df1['avg_cumsum'])
# st.pyplot(fig2)
df1.reset_index(inplace=True)

st.line_chart(data=df1, x='Date', y='avg_cumsum', use_container_width=True)
#################################################################################################################################
