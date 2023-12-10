import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
for i in range(1, 32): 
    url = f'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=&operator=AND&detailKeyword=&publicDataPk=&recmSe=&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=updtDt&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage={i}&perPage=100&brm=%EA%B3%B5%EA%B3%B5%ED%96%89%EC%A0%95%2C%EA%B5%AD%ED%86%A0%EA%B4%80%EB%A6%AC%2C%EC%82%AC%ED%9A%8C%EB%B3%B5%EC%A7%80%2C%EC%9E%AC%EC%A0%95%EA%B8%88%EC%9C%B5&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode='
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.select_one('div.result-list')
        items = div.select('ul > li')

        for item in items:
            if item.select_one('.recent-title'):
                title = item.select_one('.recent-title').get_text(strip=True).split('\n')[0]
            else:
                title = item.select_one('.title').get_text(strip=True).split('\n')[0]
            data.append(title)
    else: 
        print("Failed to fetch data on page", i)

df = pd.DataFrame(data, columns=['type'])

file_path = '/Users/kimdogyun/Downloads/data_results_type.xlsx'
df.to_excel(file_path, index=False)
