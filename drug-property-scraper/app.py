# 필요한 라이브러리를 임포트합니다.
import requests
from bs4 import BeautifulSoup

# 사용자로부터 URL과 찾고자 하는 셀렉터의 정보를 입력 받습니다.
url = input("URL을 입력하세요: ")
selector = input("찾고자 하는 셀렉터를 입력하세요 (예: '.className', '#idName', 'tag'): ")

# URL의 웹페이지를 가져옵니다.
response = requests.get(url)

# 웹페이지의 HTML을 파싱합니다.
soup = BeautifulSoup(response.text, 'html.parser')

# 지정된 셀렉터에 해당하는 모든 요소를 찾습니다.
elements = soup.select(selector)

# 찾은 요소들을 출력합니다.
for element in elements:
    print(element)
    print("--------------------------------------------------")

# 찾은 요소가 없을 경우 메시지를 출력합니다.
if not elements:
    print("지정된 셀렉터에 해당하는 요소를 찾을 수 없습니다.")
