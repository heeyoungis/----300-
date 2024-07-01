
#041
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

#042
ticker = "BTC_KRW"
ticker1 = ticker.lower()
print(ticker1)

#043
string = 'hello'
string = string.capitalize()
print(string)

#044
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

#045
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx' or 'xls'))

#046
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

#047
a = "hello world"
print(a.split())

#048
ticker = "btc_krw"
print(ticker.split('_'))

#049
date = "2020-05-01"
date = date.split('-')
print(f'연도: {date[0]} 월: {date[1]} 일: {date[2]}')

#050
data = "039490     "
data = data.rstrip()
print(data)
