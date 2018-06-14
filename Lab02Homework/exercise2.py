from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs"

conn = urlopen(url)
data = conn.read()

song_content = data.decode("utf-8")
# print(song_content)

# f = open("itunessongs.html", "wb")
# f.write(song_content)
# f.close()

soup = BeautifulSoup(song_content, "html.parser")
# print(soup.prettify())

section = soup.find("section", "section chart-grid")
# print(section.prettify())

ul = section.div.ul
# print(ul.prettify())

li_list = ul.find_all("li")

records = []

for li in li_list:
    data = {}

    h3 = li.h3
    h4 = li.h4
    data["Name"] = h3.string
    data["Artist"] = h4.string
    
    records.append(data)

pyexcel.save_as(records = records , dest_file_name = "songsdata.xlsx")



# Download

for item in records:
    option = options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
    }
    dl = YoutubeDL(options)
    dl.download([item['Name'] +" " + item["Artist"]])





