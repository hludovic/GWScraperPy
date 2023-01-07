from requests import get
from bs4 import BeautifulSoup
import csv

url = "https://wiki.guildwars.com/wiki/Daily_activities"
soup = BeautifulSoup(get(url).content, 'html.parser')
tableData = soup.find('table').find('tbody').find_all('tr')
headings = []
descriptions = []

for th in tableData[0].find_all('th'):
    headings.append(th.text.strip())

tableData.pop(0)

for cella in tableData:
    urlA = cella.find('a', href=True)['href']
    titleA = cella.find('a').text

descriptions = []
for cell in tableData:
    description = []
    for td in cell.find_all('td'):
        description.append(td.text.strip())
    descriptions.append(description)


# CSV output
with open("data.csv", "w") as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=",")
    writer.writerow(headings)
    for line in descriptions:
        writer.writerow(line)
