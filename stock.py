#!/usr/local/bin/python3.7

import tushare as ts
import yfinance as yf
import pandas as pd
import os
import datetime


today = datetime.date.today()
yesterday = datetime.date.today() + datetime.timedelta(-1)

# process US stocks by yahoo finance SDK
fo = open('./us_stock.cfg')
us_stocks = fo.read()
us_df = yf.download(us_stocks, start=yesterday.strftime('%Y-%m-%d'))
res_df = us_df.iloc[0].Close

# process Chinese stocks by tushare SDK
with open('./cn_stock.cfg') as f:
	l = f.readlines();
	for cn_stock in l:
		cn_stock = cn_stock.strip('\n')
		print(cn_stock)
		cn_df = ts.get_hist_data(cn_stock, start=yesterday.strftime('%Y-%m-%d'))
		if isinstance(cn_df, pd.DataFrame):
			print(cn_df.iloc[0].close)
			res_df[cn_stock] = cn_df.iloc[0].close
#print(res_df)

# process Hongkong stocks and Chinese fund price data 
# which are pulled from sina and Tiantian fund platform web link.
with open('./hk_and_cn_fund.res.txt') as f:
	l = f.readlines();
	for res in l:
		arr = res.split()
		res_df[arr[0]] = arr[1]
print(res_df)

# generate excel output file
res_df.to_excel('./prices.xlsx')
