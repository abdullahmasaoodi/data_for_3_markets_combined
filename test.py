# needed libs
import requests
import pandas as pd
from pandas import json_normalize
import json
from urllib.request import urlopen
import numpy as np
import streamlit as st

#################################################################################    KSA        ########################################################################################################

# main_saudi_stocks
url_main_saudi_stocks = "https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/main-market-watch/!ut/p/z1/jdBbC4JAEAXgX-Orc1Dclt4kqeimJpHtS1jYJqgb65Z_P6kno9u8zfAdOAwJSknU2a2QmSlUnZXdvhNs7_kMzpQj5EEwQjye8-kMoQM2oG0fIIm8DkRLd4E1JmAk_snjw_j4nRcvZDlhiFd-HDoDD0icV_Cm4gN86TAjIUt1eP7Drw8ulyR0fsp1ru2r7s5nYy7N0IKFtm1tqZQsc_uoKgvvImfVGEr7kpJM06XapCiiassNvwPzDnHU/p0/IZ7_IPG41I82KGASC06S67RB9A0080=CZ6_5A602H80O8DDC0QFK8HJ0O2067=NJgetMainNomucMarketDetails=/?sectorParameter=&tableViewParameter=1&iswatchListSelected=NO&requestLocale=ar&_=1710619053698"
response_main_saudi_stocks = requests.get(url_main_saudi_stocks)
data_main_saudi_stocks = response_main_saudi_stocks.json()
data_main_saudi_stocks = data_main_saudi_stocks['data']
whole_df_main_saudi_stocks = json_normalize(data_main_saudi_stocks)
whole_df_main_saudi_stocks["market_type"] = "الأسهم - السوق الرئيسية"
whole_df_main_saudi_stocks["market"] = "السوق السعودي"
summary_df_main_saudi_stocks = whole_df_main_saudi_stocks[
    ["companyUrl", "acrynomName", "companyRef", "lastTradePrice", "market", "market_type"]]

# saudi_funds
url_saudi_funds = "https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/funds-market-watch/mutual-funds/!ut/p/z1/lc9NDoIwFATgs3AA06Ha0m0jCKJYSkWxG9OVaaJojPH8EncEf9_uJd8kM8SShtjW3f3B3fy5dcfu31m-Z5KDZgJKJVEEPVurcBMmdFJxsu0DUaQceiW1ohEDDCX2rzxMyTpQFuMlKqTgv-Xx5iS-522fiDiedmQhshyKIg8HYDixD15seIIPJY27ksuprhv4-UgGwQPkM992/p0/IZ7_5A602H80OOMQC0604RU6VD1067=CZ6_5A602H80OOE770QFTO1V1E24R6=NJgetMutualFundsData=/"
response_saudi_funds = requests.get(url_saudi_funds)
data_saudi_funds = response_saudi_funds.json()
data_saudi_funds = data_saudi_funds['data']
whole_df_saudi_funds = json_normalize(data_saudi_funds)
whole_df_saudi_funds["market_type"] = "صناديق"
whole_df_saudi_funds["market"] = "السوق السعودي"
whole_df_saudi_funds["sectorName"] = "-"
summary_df_saudi_funds = whole_df_saudi_funds[
    ["companyUrl", "fundName", "symbol", "unitPrice", "market", "market_type"]]

# parallel_saudi_stocks
url_parallel_saudi_stocks = "https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/nomuc-market-watch/!ut/p/z1/lZDLDoIwEEW_xQVb5ooBG3eNRo0vQGLEbgwarCRATa3y-xJd-dbZzeSc5M4lQTGJMjlnMjGZKpO83lfCW7vcgzNk8Fmv10XYH7PhCL6DJmj5AEwHHsIZD32n7QKRQ-IvH1Hg1kAwbU0wxwDebz7eDMd3Xzwgzx_cAy8iXoEPGUYkZK42tz55uWkxSUKnu1Sn2j7p-rw35nDsWLBQVZUtlZJ5am9VYeGVsldHQ_E9SVGi6VAsFjGyoFgyw3ijcQE05jai/p0/IZ7_IPG41I82KGASC06S67RB9A0041=CZ6_5A602H80O8DDC0QFK8HJ0O2010=NJgetMainNomucMarketDetails=/?sectorParameter=&tableViewParameter=1&iswatchListSelected=NO&requestLocale=ar&_=1710619161193"
response_parallel_saudi_stocks = requests.get(url_parallel_saudi_stocks)
data_parallel_saudi_stocks = response_parallel_saudi_stocks.json()
data_parallel_saudi_stocks = data_parallel_saudi_stocks['data']
whole_df_parallel_saudi_stocks = json_normalize(data_parallel_saudi_stocks)
whole_df_parallel_saudi_stocks["market_type"] = "الأسهم - السوق الموازية"
whole_df_parallel_saudi_stocks["market"] = "السوق السعودي"
summary_df_parallel_saudi_stocks = whole_df_parallel_saudi_stocks[
    ["companyUrl", "acrynomName", "companyRef", "lastTradePrice", "market", "market_type"]]

# saudi_bonds_and_sukuk
url_saudi_bonds_and_sukuk = "https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/sukuk-market-watch/!ut/p/z1/lZBBb4JAEIV_iweuzAuG7cbbpkSNVoESAu6lwQZXEmDNssrfL2lPom11bjP5vuTNI0k5yba4VKqwlW6Leth3kn34gsFbcoQ8CF4Rz9d8uULoIWCUjYDNgiHeijj0Xnwg8Ug-5SOJ_AGINtM3vGMB9piPX0bgf1-OkNsProE7Eb-BPzKsSKpa73_6FO1-yhVJUx5KUxr3bIbz0dpTN3PgoO97V2mt6tL91I2De8pRd5bya5KSwtCpSdMcVdRk3HIxmXwBPTPbCA!!/p0/IZ7_5A602H80OOMQC0604RU6VD1091=CZ6_5A602H80O8DDC0QFK8HJ0O20D6=NJgetSukukMarketDetails=/?sectorParameter=all&iswatchListSelected=NO&requestLocale=ar&_=1710619264360"
response_saudi_bonds_and_sukuk = requests.get(url_saudi_bonds_and_sukuk)
data_saudi_bonds_and_sukuk = response_saudi_bonds_and_sukuk.json()
data_saudi_bonds_and_sukuk = data_saudi_bonds_and_sukuk['data']
whole_df_saudi_bonds_and_sukuk = json_normalize(data_saudi_bonds_and_sukuk)
whole_df_saudi_bonds_and_sukuk["market_type"] = "الصكوك و السندات"
whole_df_saudi_bonds_and_sukuk["market"] = "السوق السعودي"
whole_df_saudi_funds["sectorName"] = "-"
summary_df_saudi_bonds_and_sukuk = whole_df_saudi_bonds_and_sukuk[
    ["cUrl", "issuerName", "symbol", "lastTradePrice", "market", "market_type"]]

#### renaming the colmns names for all DFs  ################

summary_df_main_saudi_stocks = summary_df_main_saudi_stocks.rename(columns={
    "companyUrl": "الرابط",
    "acrynomName": "الاسم",
    "companyRef": "الرمز",
    "lastTradePrice": "آخر سعر",
    "market": "السوق",
    "market_type": "نوع الجهة"
})
summary_df_saudi_funds = summary_df_saudi_funds.rename(columns={
    "companyUrl": "الرابط",
    "fundName": "الاسم",
    "symbol": "الرمز",
    "unitPrice": "آخر سعر",
    "market": "السوق",
    "market_type": "نوع الجهة"
})
summary_df_parallel_saudi_stocks = summary_df_parallel_saudi_stocks.rename(columns={
    "companyUrl": "الرابط",
    "acrynomName": "الاسم",
    "companyRef": "الرمز",
    "lastTradePrice": "آخر سعر",
    "market": "السوق",
    "market_type": "نوع الجهة"
})
summary_df_saudi_bonds_and_sukuk = summary_df_saudi_bonds_and_sukuk.rename(columns={
    "cUrl": "الرابط",
    "issuerName": "الاسم",
    "symbol": "الرمز",
    "lastTradePrice": "آخر سعر",
    "market": "السوق",
    "market_type": "نوع الجهة"
})

#### combining all DFs  from saudi markets ################

summary_combined_all_saudi_dfs = pd.concat(
    [summary_df_main_saudi_stocks, summary_df_saudi_funds, summary_df_parallel_saudi_stocks,
     summary_df_saudi_bonds_and_sukuk])

#################################################################################    UAE        ########################################################################################################
# for Dubai_market

url_dubai_market_for_prices = "https://marketwatch.dfm.ae/dapi/fetch"

# responses for prices
# Dubai Market Prices Request
url_dubai_market_for_prices = "https://marketwatch.dfm.ae/dapi/fetch"
payload_for_prices = json.dumps([
    {
        "id": "de5f4d6c-131e-eac7-ef04-116c83f667bc",
        "command": "stocks",
        "data": [
            {
                "id": "lastrefreshtime",
                "value": "0"
            },
            {
                "id": "id",
                "value": ""
            }
        ]
    }
])
headers_for_prices = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en,ar;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': '_ga_8FYMXRNZGJ=GS1.1.1715791938.1.0.1715791938.0.0.0; _ga=GA1.2.1969993828.1715791939; _gid=GA1.2.1482773242.1715791939; ASP.NET_SessionId=dv5rfamjvybhn4myvkrsw5ec; marketwatch=ffffffffaf1c0d9045525d5f4f58455e445a4a423660; _ga=GA1.3.1969993828.1715791939; _gid=GA1.3.1482773242.1715791939; _gat=1; _ga_SC1494TPQB=GS1.3.1715795006.1.1.1715795115.0.0.0; dimensions=; ASP.NET_SessionId=ah5kkq3cl5xoduphybwstdfb; marketwatch=ffffffffaf1c0d6e45525d5f4f58455e445a4a423660',
    'Origin': 'https://marketwatch.dfm.ae',
    'Referer': 'https://marketwatch.dfm.ae/ar',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-KL-saas-Ajax-Request': 'Ajax_Request',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}
response_dubai_market_for_prices = requests.post(url_dubai_market_for_prices, headers=headers_for_prices,
                                                 data=payload_for_prices)

# Dubai Market Information Request
url_dubai_market_for_information = "https://marketwatch.dfm.ae/api/fetch"
payload_for_information = json.dumps([
    {
        "id": "86af600d-5fcc-b338-ef9f-6545d311b16c",
        "command": "sitefinity_securities",
        "data": [
            {
                "id": "language",
                "value": "ar"
            }
        ]
    },
    {
        "id": "0aae714b-f785-363d-be70-7ffb97bd1e25",
        "command": "news",
        "data": [
            {
                "id": "language",
                "value": "ar"
            }
        ]
    },
    {
        "id": "8d0f5084-55ae-2122-c3a6-38e9b24320a1",
        "command": "sitefinity_sectors",
        "data": [
            {
                "id": "language",
                "value": "ar"
            }
        ]
    },
    {
        "id": "cab49902-a62a-77ee-297c-c42e075acb94",
        "command": "sitefinity_exchanges",
        "data": [
            {
                "id": "language",
                "value": "ar"
            }
        ]
    },
    {
        "id": "295fe55d-8833-4b2f-7cca-c6292c822bd4",
        "command": "sitefinity_sectors",
        "data": [
            {
                "id": "language",
                "value": "ar"
            }
        ]
    }
])
headers_for_information = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en,ar;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': '_ga=GA1.2.1969993828.1715791939; ASP.NET_SessionId=dv5rfamjvybhn4myvkrsw5ec; marketwatch=ffffffffaf1c0d9045525d5f4f58455e445a4a423660; _ga=GA1.3.1969993828.1715791939; _ga_8FYMXRNZGJ=GS1.1.1715795190.2.0.1715795190.0.0.0; _gid=GA1.3.1126423646.1716057679; _gat=1; _ga_SC1494TPQB=GS1.3.1716057679.4.1.1716057829.0.0.0; dimensions=',
    'Origin': 'https://marketwatch.dfm.ae',
    'Referer': 'https://marketwatch.dfm.ae/ar',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-KL-saas-Ajax-Request': 'Ajax_Request',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}
response_dubai_market_for_information = requests.post(url_dubai_market_for_information, headers=headers_for_information,
                                                      data=payload_for_information)

# Parse responses
data_dubai_market_for_information = response_dubai_market_for_information.json()
extract_from_data_dubai_market_for_information = data_dubai_market_for_information[0]['data']
whole_df_dubai_market_for_information = pd.DataFrame(extract_from_data_dubai_market_for_information)
summary_df_dubai_market_for_information = whole_df_dubai_market_for_information[["id", "fullName", "securityType"]]

data_dubai_market_for_prices = response_dubai_market_for_prices.json()
extract_from_data_dubai_market_for_prices = data_dubai_market_for_prices[0]['data']
whole_df_dubai_market_for_prices = pd.DataFrame(extract_from_data_dubai_market_for_prices)
whole_df_dubai_market_for_prices["market"] = "سوق دبي المالي - DFM"
whole_df_dubai_market_for_prices["cUrl"] = ""
summary_df_dubai_market_for_prices = whole_df_dubai_market_for_prices[["cUrl", "id", "lastradeprice", "market"]]

# Merge DataFrames
summary_of_2DFs_dubai_market = pd.merge(
    summary_df_dubai_market_for_prices,
    summary_df_dubai_market_for_information[["id", "fullName", "securityType"]],
    on="id",
    how="left"
)

summary_of_2DFs_dubai_market = summary_of_2DFs_dubai_market[
    ["cUrl", "fullName", "id", "lastradeprice", "market", "securityType"]]

#######################################

# 5B- for abu_dhabi_market

url_abu_dhabi_market = "https://apiwebservices.adx.ae/ds/mwdelay"
response_abu_dhabi_market = requests.get(url_abu_dhabi_market)
data_abu_dhabi_market = response_abu_dhabi_market.json()

whole_df_abu_dhabi_market = json_normalize(data_abu_dhabi_market)
whole_df_abu_dhabi_market["market"] = "سوق أبو ظبي المالي - ADX"
whole_df_abu_dhabi_market["market_type"] = "الأسهم - السوق الرئيسية"

whole_df_abu_dhabi_market["cUrl"] = ""
summary_df_abu_dhabi_market = whole_df_abu_dhabi_market[
    ["cUrl", "ARBCOMPANYNAME", "Symbol", "Last", "market", "SectorArb"]]

# this step for renaming the abo dhabai df to be matching the dubai df
summary_df_abu_dhabi_market = summary_df_abu_dhabi_market.rename(columns={
    "ARBCOMPANYNAME": "fullName",
    "Symbol": "id",
    "Last": "lastradeprice",
    "SectorArb": "securityType"
})

url_abu_dhabi_market = "https://apiwebservices.adx.ae/ds/mwdelay"
response_abu_dhabi_market = requests.get(url_abu_dhabi_market)
data_abu_dhabi_market = response_abu_dhabi_market.json()

whole_df_abu_dhabi_market = json_normalize(data_abu_dhabi_market)
whole_df_abu_dhabi_market["market"] = "سوق أبو ظبي المالي - ADX"

whole_df_abu_dhabi_market["SectorArb"] = np.where(
    whole_df_abu_dhabi_market["SectorArb"] != "آخر",
    "الأسهم - السوق الرئيسية",
    "آخر"
)

whole_df_abu_dhabi_market["cUrl"] = ""
summary_df_abu_dhabi_market = whole_df_abu_dhabi_market[
    ["cUrl", "ARBCOMPANYNAME", "Symbol", "Last", "market", "SectorArb"]]

# this step for renaming the abo dhabai df to be matching the dubai df
summary_df_abu_dhabi_market = summary_df_abu_dhabi_market.rename(columns={
    "ARBCOMPANYNAME": "fullName",
    "Symbol": "id",
    "Last": "lastradeprice",
    "SectorArb": "securityType"
})

#######################################
#######################################
#######################################

# Combined data for UAE markets

summary_df_of_UAE_dubai_and_abu_dhabi = pd.concat([summary_df_abu_dhabi_market, summary_of_2DFs_dubai_market])

summary_df_of_UAE_dubai_and_abu_dhabi = summary_df_of_UAE_dubai_and_abu_dhabi.rename(columns={
    "cUrl": "الرابط",
    "fullName": "الاسم",
    "id": "الرمز",
    "lastradeprice": "آخر سعر",
    "market": "السوق",
    "securityType": "نوع الجهة"
})

#################################################################################    QATAR        ########################################################################################################
# for qatar market

url_qatar_markets = "https://www.qe.com.qa/wp/mw/bg/mw.php"

payload = 'f=MarketWatch'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en,ar;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'GUEST_LANGUAGE_ID=ar_SA; COOKIE_SUPPORT=true; _ga=GA1.3.1655899438.1717096457; TS011739b0=0166cb97e49d2b6a4cbbf1bd14a0720f34def0d52cbe12226efa2e7db44f546b8666cea16c49b88d026912ce5b80c3d2cd5982632b; JSESSIONID=CF47FC3C9B394FD7CCF7ADDE325F0C70; TS01b30ae4=0166cb97e4fc51109167109e1e1889780ae5c6834517cf0ba363e1c5c67edae77452b013c167c4a9105ce380f362fdee971eb66f965f8bcb68d22be865fe85060dba34e4cae7d4af68a206b8209efffbbd66660ae7; _gid=GA1.3.958024764.1718130991; _ga_WF5BK0MYBM=GS1.3.1718130991.3.0.1718130991.60.0.0; LFR_SESSION_STATE_20158=1718130996405; TS9afc51c1027=084d1c6a81ab200072c9e6fd208a5ddf89792a2e50016f78a28cdacd5664600a5ee7f4952e28e51808ff0b6e63113000033b43f2038ddbb089d40eb59d0138b0a094f6e8fb8ea9d6555df27046e948429f486163cd52144722ddd8cbc3312b50; TS011739b0=0166cb97e452532ecedf21392c1b89c0287c748d8519c999b39d6bf9d56b536a2037c3c4ad9d95a8910c8fdbe901fefbca36a8f768; TS9afc51c1027=084d1c6a81ab2000a59146dd13e07f4241865967cf47564152e0df04bf3d6f111e71b37db75a3e9308ab7aaf7b113000fb1eb99bea17dc3da405aeceda8a1395ab3b18615597766260066cb7ff470fd3896fe6969acbba70c00cc07d1fb0fd2d',
    'Origin': 'https://www.qe.com.qa',
    'Referer': 'https://www.qe.com.qa/wp/mws/market/main',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'X-KL-saas-Ajax-Request': 'Ajax_Request',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

response_qatar_markets = requests.request("POST", url_qatar_markets, headers=headers, data=payload)
data_qatar_markets = response_qatar_markets.json()
whole_df_qatar_market = pd.DataFrame(data_qatar_markets['rows'])
whole_df_qatar_market["market"] = "سوق قطر المالي"
whole_df_qatar_market["cUrl"] = "-"

whole_df_qatar_market.loc[whole_df_qatar_market["CompType"] == "COMP", "market_type"] = "الأسهم - السوق الرئيسية"
whole_df_qatar_market.loc[whole_df_qatar_market["CompType"] == "BOND", "market_type"] = "الصكوك و السندات"
whole_df_qatar_market.loc[whole_df_qatar_market["CompType"] == "ETF", "market_type"] = "صناديق"
whole_df_qatar_market.loc[whole_df_qatar_market["CompType"] == "V", "market_type"] = "سوق الشركات الناشئة"

summary_df_qatar_market = whole_df_qatar_market[["cUrl", "CompanyAR", "Symbol", "LastPrice", "market", "market_type"]]

summary_df_qatar_market = summary_df_qatar_market.rename(columns={
    "cUrl": "الرابط",
    "CompanyAR": "الاسم",
    "Symbol": "الرمز",
    "LastPrice": "آخر سعر",
    "market": "السوق",
    "market_type": "نوع الجهة"
})

######################################################################################## the_final_resulted_df  ###########################################################################################################
the_final_resulted_df = pd.concat(
    [summary_combined_all_saudi_dfs, summary_df_of_UAE_dubai_and_abu_dhabi, summary_df_qatar_market])
the_final_resulted_df['الرمز'] = the_final_resulted_df['الرمز'].astype(str)
the_final_resulted_df['آخر سعر'] = the_final_resulted_df['آخر سعر'].astype(float)

######################################################################################## showing_the_final_resulted_df_at_web_page  ###########################################################################################################
st.dataframe(the_final_resulted_df)
