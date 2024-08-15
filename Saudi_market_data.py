# needed libs
import requests
import pandas as pd
from pandas import json_normalize
import json
from urllib.request import urlopen
import numpy as np
import streamlit as st
import dash
import dash_table
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html



#################################################################################    KSA        ########################################################################################################

# main_saudi_stocks
url_main_saudi_stocks = "https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/main-market-watch/!ut/p/z1/jdBbC4JAEAXgX-Orc1Dclt4kqeimJpHtS1jYJqgb65Z_P6kno9u8zfAdOAwJSknU2a2QmSlUnZXdvhNs7_kMzpQj5EEwQjye8-kMoQM2oG0fIIm8DkRLd4E1JmAk_snjw_j4nRcvZDlhiFd-HDoDD0icV_Cm4gN86TAjIUt1eP7Drw8ulyR0fsp1ru2r7s5nYy7N0IKFtm1tqZQsc_uoKgvvImfVGEr7kpJM06XapCiiassNvwPzDnHU/p0/IZ7_IPG41I82KGASC06S67RB9A0080=CZ6_5A602H80O8DDC0QFK8HJ0O2067=NJgetMainNomucMarketDetails=/?sectorParameter=&tableViewParameter=1&iswatchListSelected=NO&requestLocale=ar&_=1710619053698"
response_main_saudi_stocks = requests.get(url_main_saudi_stocks)
data_main_saudi_stocks = response_main_saudi_stocks.json()
data_main_saudi_stocks = data_main_saudi_stocks['data']
whole_df_main_saudi_stocks = json_normalize(data_main_saudi_stocks)
whole_df_main_saudi_stocks["market_type"] = "الأسهم - السوق الرئيسية"
whole_df_main_saudi_stocks["market"] = "السوق السعودي"
summary_df_main_saudi_stocks = whole_df_main_saudi_stocks[["companyUrl", "acrynomName",  "companyRef","lastTradePrice","market","market_type"]]

# saudi_funds
url_saudi_funds = "https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/funds-market-watch/mutual-funds/!ut/p/z1/lc9NDoIwFATgs3AA06Ha0m0jCKJYSkWxG9OVaaJojPH8EncEf9_uJd8kM8SShtjW3f3B3fy5dcfu31m-Z5KDZgJKJVEEPVurcBMmdFJxsu0DUaQceiW1ohEDDCX2rzxMyTpQFuMlKqTgv-Xx5iS-522fiDiedmQhshyKIg8HYDixD15seIIPJY27ksuprhv4-UgGwQPkM992/p0/IZ7_5A602H80OOMQC0604RU6VD1067=CZ6_5A602H80OOE770QFTO1V1E24R6=NJgetMutualFundsData=/"
response_saudi_funds = requests.get(url_saudi_funds)
data_saudi_funds = response_saudi_funds.json()
data_saudi_funds = data_saudi_funds['data']
whole_df_saudi_funds = json_normalize(data_saudi_funds)
whole_df_saudi_funds["market_type"] = "صناديق"
whole_df_saudi_funds["market"] = "السوق السعودي"
whole_df_saudi_funds["sectorName"] = "-"
summary_df_saudi_funds = whole_df_saudi_funds[["companyUrl", "fundName",  "fundCode",  "unitPrice","market","market_type"]]


# parallel_saudi_stocks
url_parallel_saudi_stocks = "https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/nomuc-market-watch/!ut/p/z1/lZDLDoIwEEW_xQVb5ooBG3eNRo0vQGLEbgwarCRATa3y-xJd-dbZzeSc5M4lQTGJMjlnMjGZKpO83lfCW7vcgzNk8Fmv10XYH7PhCL6DJmj5AEwHHsIZD32n7QKRQ-IvH1Hg1kAwbU0wxwDebz7eDMd3Xzwgzx_cAy8iXoEPGUYkZK42tz55uWkxSUKnu1Sn2j7p-rw35nDsWLBQVZUtlZJ5am9VYeGVsldHQ_E9SVGi6VAsFjGyoFgyw3ijcQE05jai/p0/IZ7_IPG41I82KGASC06S67RB9A0041=CZ6_5A602H80O8DDC0QFK8HJ0O2010=NJgetMainNomucMarketDetails=/?sectorParameter=&tableViewParameter=1&iswatchListSelected=NO&requestLocale=ar&_=1710619161193"
response_parallel_saudi_stocks = requests.get(url_parallel_saudi_stocks)
data_parallel_saudi_stocks = response_parallel_saudi_stocks.json()
data_parallel_saudi_stocks = data_parallel_saudi_stocks['data']
whole_df_parallel_saudi_stocks = json_normalize(data_parallel_saudi_stocks)
whole_df_parallel_saudi_stocks["market_type"] = "الأسهم - السوق الموازية"
whole_df_parallel_saudi_stocks["market"] = "السوق السعودي"
summary_df_parallel_saudi_stocks = whole_df_parallel_saudi_stocks[["companyUrl", "acrynomName",  "companyRef","lastTradePrice","market","market_type"]]

# saudi_bonds_and_sukuk
url_saudi_bonds_and_sukuk = "https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/sukuk-market-watch/!ut/p/z1/lZBBb4JAEIV_iweuzAuG7cbbpkSNVoESAu6lwQZXEmDNssrfL2lPom11bjP5vuTNI0k5yba4VKqwlW6Leth3kn34gsFbcoQ8CF4Rz9d8uULoIWCUjYDNgiHeijj0Xnwg8Ug-5SOJ_AGINtM3vGMB9piPX0bgf1-OkNsProE7Eb-BPzKsSKpa73_6FO1-yhVJUx5KUxr3bIbz0dpTN3PgoO97V2mt6tL91I2De8pRd5bya5KSwtCpSdMcVdRk3HIxmXwBPTPbCA!!/p0/IZ7_5A602H80OOMQC0604RU6VD1091=CZ6_5A602H80O8DDC0QFK8HJ0O20D6=NJgetSukukMarketDetails=/?sectorParameter=all&iswatchListSelected=NO&requestLocale=ar&_=1710619264360"
response_saudi_bonds_and_sukuk = requests.get(url_saudi_bonds_and_sukuk)
data_saudi_bonds_and_sukuk = response_saudi_bonds_and_sukuk.json()
data_saudi_bonds_and_sukuk = data_saudi_bonds_and_sukuk['data']
whole_df_saudi_bonds_and_sukuk = json_normalize(data_saudi_bonds_and_sukuk)
whole_df_saudi_bonds_and_sukuk["market_type"] = "الصكوك و السندات"
whole_df_saudi_bonds_and_sukuk["market"] = "السوق السعودي"
whole_df_saudi_funds["sectorName"] = "-"
summary_df_saudi_bonds_and_sukuk = whole_df_saudi_bonds_and_sukuk[["cUrl", "issuerName", "symbol", "lastTradePrice", "market","market_type"]]


#### renaming the colmns names for all DFs  ################

summary_df_main_saudi_stocks = summary_df_main_saudi_stocks.rename(columns={
    "companyUrl" : "الرابط",
    "acrynomName" : "الاسم",
    "companyRef" : "الرمز",
    "lastTradePrice" : "آخر سعر" ,
    "market" : "السوق",
    "market_type" : "نوع الجهة"
})
summary_df_saudi_funds = summary_df_saudi_funds.rename(columns={
    "companyUrl" : "الرابط",
    "fundName" : "الاسم",
    "fundCode" : "الرمز",
    "unitPrice" : "آخر سعر" ,
    "market" : "السوق",
    "market_type" : "نوع الجهة"
})
summary_df_parallel_saudi_stocks = summary_df_parallel_saudi_stocks.rename(columns={
    "companyUrl" : "الرابط",
    "acrynomName" : "الاسم",
    "companyRef" : "الرمز",
    "lastTradePrice" : "آخر سعر" ,
    "market" : "السوق",
    "market_type" : "نوع الجهة"
})
summary_df_saudi_bonds_and_sukuk = summary_df_saudi_bonds_and_sukuk.rename(columns={
    "cUrl" : "الرابط",
    "issuerName" : "الاسم",
    "symbol" : "الرمز",
    "lastTradePrice" : "آخر سعر" ,
    "market" : "السوق",
    "market_type" : "نوع الجهة"
})

#### combining all DFs  from saudi markets ################

summary_combined_all_saudi_dfs = pd.concat([summary_df_main_saudi_stocks,summary_df_saudi_funds,summary_df_parallel_saudi_stocks,summary_df_saudi_bonds_and_sukuk])

app = dash.Dash(__name__)
app.layout = html.Div([
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in summary_combined_all_saudi_dfs.columns],
        data=summary_combined_all_saudi_dfs.to_dict('records'),
    )
])

if __name__ == '__main__':
    app.run_server(port=8052, debug=False)
