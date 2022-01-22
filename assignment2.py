from urllib.request import urlopen
from bs4 import BeautifulSoup

file = open("/music.txt", "w")

html = urlopen("https://music.bugs.co.kr/chart?wl_ref=M_left_02_01")
soup = BeautifulSoup(html, "lxml")
musicList = soup.find_all("p",{'class':'title'})
for music in musicList:
    print(music.get_text())
    file.write(music)

file.close()
