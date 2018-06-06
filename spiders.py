import requests, csv
from bs4 import BeautifulSoup



headers = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

play_url ='http://music.163.com/playlist?id=xxxxxx'

s = requests.session()
s = BeautifulSoup(s.get(play_url,headers = headers).content)
main = s.find('ul', {'class': 'f-hide'})

musicarr = []
for music in main.find_all('a'):
    musicarr.append([music.text, r'https://music.163.com/#'+ music['href']])

#writes files
def writes(paths):
    with open(paths, "w", newline="", encoding='utf-8') as newFileObj:
        try:
            csvWriter = csv.writer(newFileObj, dialect='excel')
            csvWriter.writerows(musicarr)
        finally:
            newFileObj.close()

writes('./musiclist.csv')
