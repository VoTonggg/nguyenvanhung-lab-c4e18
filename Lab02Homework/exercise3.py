from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)

data = conn.read()

html_content = data.decode("utf-8")

# f = open("hose_data.html", "wb") 
# f.write(html_content)
# f.close()

soup = BeautifulSoup(html_content, "html.parser")

records = []

div_table_header = soup.find("div" , id = "divTableHeader")
# print(div_table_header)

div_table_content = soup.find("div", style = "overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
# print(div_table_content)

# tr_table_header = div_table_header.table.tr
# # print(tr_table_header.prettify())
# td_list = tr_table_header.find_all("td")
# data = {}
# data[td_list[0].string] = []
# for i in range(1,5):
#     data[td_list[0].string].append(td_list[i].string)

# records.append(data)

table_content = div_table_content.table
# print(table_content.prettify())

tr_table_content_list = table_content.find_all("tr")

for tr in tr_table_content_list:
    print(tr)
    # td_list = tr.find_all("td")
    # data = {}
    # values = []
    # for j in range(1, 5):
    #     print(j)
    #     values.append(td_list[j].string)
    #     print(j)
    # data[td_list[0].string] = values
    # print(data)
    # records.append(data)
    

