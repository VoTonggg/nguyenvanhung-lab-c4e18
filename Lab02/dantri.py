from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://dantri.com.vn"
# 1. Download webpage
# 1.1 Create a connection
# conn = urlopen(url)
# 1.2 Read
# data = conn.read()
# print(data)
# # 1.3 Decode
# html_content = data.decode("utf-8")
html_content = urlopen(url).read().decode("utf-8")
# print(html_content) 

# Save html_content to file
# f = open("dantri.html", "wb")
# f.write(html_content)
# f.close()

# 2. Extract the ROI (region of interest)
#html xml xhtml
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())

ul = soup.find("ul", "ul1 ulnew")
# print(ul.prettify())


li_list = ul.find_all("li")

# 3. Extract info
records = []

for li in li_list:
    # print(li.prettify())
    # print("* " * 20)
    # h4 = li.find("h4")
    # a = h4.find("a")
    data = {}
    a = li.h4.a
    data["title"] = a.string
    data["link"] = url + a["href"]
    records.append(data)

print(records)
pyexcel.save_as(records = records, dest_file_name = "dantri.xlsx")