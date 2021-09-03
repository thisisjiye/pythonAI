import warnings
warnings.filterwarnings(action='ignore')
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

print(dt.now())

targetSite = 'https://music.bugs.co.kr/chart'
request = requests.get(targetSite)
# print(request)
html = request.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# 노래 제목 크롤링
titles = soup.findAll('p', {'class': 'title'})
# print(titles)
# print(len(titles))

for i in range(len(titles)):
    # print('{0:3d}위 {1}'.format(i + 1, titles[i].text.strip()))
    # print('{0:3d}위 {1}'.format(i + 1, titles[i].text.split('\n')[1]))
    print('{0:3d}위 {1}'.format(i + 1, titles[i].text.strip().split('\n')[0]))

# 아티스트 크롤링
artists = soup.findAll('p', {'class': 'artist'})
# print(artists)
# print(len(artists))

for i in range(len(artists)):
    # print(artists[i].text.strip())
    # print(artists[i].text.split('\n'))
    print('{0:3d}위 {1}'.format(i + 1, artists[i].text.strip().split('\n')[0]))

print(dt.now())
for i in range(100):
    artist = artists[i].text.strip().split('\n')[0]
    title = titles[i].text.strip().split('\n')[0]
    print('{0:3d}위 {1} - {2}'.format(i + 1, artist, title))

# 크롤링한 결과를 텍스트 파일로 저장한다.
file = open('./output/bugsTOP100.txt', 'w')
# 위의 문장처럼 실행했는데 에러가 발생하면 아래와 같이 open() 함수를 수정한다.
# file = open('./output/bugsTOP100.txt', 'w', -1, 'UTF-8')
file.write('{} 현재 Bugs 뮤직 실시간 TOP 100\n'.format(dt.now()))
for i in range(100):
    artist = artists[i].text.strip().split('\n')[0]
    title = titles[i].text.strip().split('\n')[0]
    file.write('{0:3d}위 {1} - {2}\n'.format(i + 1, artist, title))
file.close()
print('bugsTOP100.txt 파일로 쓰기 완료')

# 텍스트 파일에 저장된 데이터를 읽어서 화면에 출력한다.
try:
    file = open('./output/bugsTOP100.txt', 'r')
    lines = file.readlines()
    for line in lines:
        print(line.strip())
    file.close()
    print('bugsTOP100.txt 파일에서 읽기 완료')
except FileNotFoundError:
    print('디스크에 bugsTOP100.txt 파일이 없습니다.')