# stock
获取指定股票、基金的价格，支持A股、美股、港股

股票代码配置信息：
- 港股：hk_stock.cfg
- 美股：us_stock.cfg
- A股股票：cn_stock.cfg
- 国内基金：cn_fund.cfg

美股从yahoo finance SDK获取数据
港股从新浪获取数据
A股从Tushare获取数据
国内基金，从天天基金网获取数据

Dependencies
=========
python 2.x/3.x   

[pandas](http://pandas.pydata.org/ "pandas")

[tushare](https://github.com/waditu/tushare)

[yfinance](https://github.com/ranaroussi/yfinance)


