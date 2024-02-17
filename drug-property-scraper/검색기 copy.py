import requests
from bs4 import BeautifulSoup
import pandas as pd

# 사용자로부터 엔터로 구분된 약품 이름들을 입력받습니다.
print("검색어를 입력하세요 (빈칸 후 엔터로 구분, 종료하려면 그냥 엔터): ")

medicine_names = []
while True:
    input_name = input()
    if input_name == "":
        break
    medicine_names.append(input_name.strip())

    print("\n현재까지 입력한 약품 목록:")
    for idx, name in enumerate(medicine_names, start=1):
        print(f"{idx}. {name}")
    print("계속 입력하거나, 종료하려면 그냥 엔터를 누르세요.")

# 결과를 저장할 데이터프레임 리스트
df_list = []

for medicine_name in medicine_names:
    encoded_medicine_name = requests.utils.quote(medicine_name)
    url = f"https://nedrug.mfds.go.kr/searchDrug?sort=&sortOrder=false&searchYn=true&ExcelRowdata=&page=1&searchDivision=detail&itemName={encoded_medicine_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 성분명만 추출합니다. 이 부분에서 properties 변수를 정의해야 합니다.
    search_property = soup.select("#con_body > div.mediWrap.m-search > div.r_sec_md > div.table_scroll > table > tbody > tr > td:nth-child(12) > span:nth-child(2)")
    properties = [tag.get_text(strip=True) for tag in search_property[:2]]  # 여기서 properties 정의

    for property in properties:
        temp_df = pd.DataFrame({'No': [medicine_names.index(medicine_name) + 1], '검색어': [medicine_name], '결과값': [property]})
        df_list.append(temp_df)

# 모든 임시 데이터프레임을 하나로 합칩니다.
df_results = pd.concat(df_list, ignore_index=True)

# 결과 데이터프레임을 CSV 파일로 저장
df_results.to_csv("medicine_search_results.csv", index=False, encoding='utf-8-sig')

print("결과가 'medicine_search_results.csv' 파일에 저장되었습니다.")
