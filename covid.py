from bs4 import BeautifulSoup
import requests
import json
import matplotlib.pyplot as plt

URL = "https://www.worldometers.info/coronavirus/country/brazil/"

parsed_html = requests.get(URL)
soup = BeautifulSoup(parsed_html.content, "html.parser")

#print(soup)

scripts = soup.find_all('script')
script = scripts[19].text


dates = script.split("categories: [",1)[1].split("]",1)[0]
dates = "["+dates+"]"
dates = json.loads(dates)
#print(dates)
# Jan 01, 2021
#print(dates[321]) 

data = script.split("data: [",1)[1].split("]",1)[0]
data = "["+data+"]"
data = json.loads(data)
#print(data)
#print(data[0])

f, ax = plt.subplots(figsize=(18,5))
ax.set_title('Pessoas infectadas x dia (Brasil)')
ax.set_xlabel('Data')
ax.set_ylabel('Quantidade de pessoas')
plt.plot(dates[321:],data[321:])

# format x-axis labels
every_nth = 10
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)

plt.show()
