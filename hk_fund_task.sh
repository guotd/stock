#!/bin/bash

FILE_NAME="hk_and_cn_fund.res.txt"
if [[ -f $FILE_NAME ]]; then
	echo "remove old file: $FILE_NAME"
	rm -f $FILE_NAME
fi

# get price data of hongkong stocks from sina 
for s in `cat hk_stock.cfg `
do 
	hk=${s%%#*}; 
	price=`curl "https://stock.finance.sina.com.cn/hkstock/api/openapi.php/HK_StockService.getHKPriceSummarize?symbol=$hk" 2>/dev/null| jq '.result.data[0].price'`
	price=`echo $price | tr -d '"'`
	echo "${hk}.HK ${price}" >> $FILE_NAME
done

# get price data of Chinese fund from easymoney platform
for f in `cat cn_fund.cfg `
do 
	price=`curl "http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=$f" 2>/dev/null | awk -F'<td' '{print $3}' |tr -cd "[0-9\.]"`
	echo "${f} $price" >> $FILE_NAME
done

echo "generate file $FILE_NAME:"
cat $FILE_NAME