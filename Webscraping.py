import requests
from bs4 import BeautifulSoup
url = "http://ttdkl.dtam.moph.go.th/Dic_chai/frmc_dictionnary_ch.aspx"
web_data = requests.get(url)
# print(web_data.text)

soup = BeautifulSoup(web_data.text,'html.parser')
find_word = soup.find_all("td")

for i in find_word:
    i = str(i).split('<td><font color="#333333" size="4">')
    i = str(i).split('</font></td>')[0]
    print(i)