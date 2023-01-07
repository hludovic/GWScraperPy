import json
from requests import get
from bs4 import BeautifulSoup

url = "https://wiki.guildwars.com/wiki/Daily_activities"
soup = BeautifulSoup(get(url).content, 'html.parser')
tableData = soup.find('table').find('tbody').find_all('tr')
headings = []
descriptions = []

# Load headings
for th in tableData[0].find_all('th'):
    headings.append(th.text.strip())

# Remove headins from tableData
tableData.pop(0)

# load descriptions
for line in tableData:
    cells = line.find_all('td')
    dictionnaryLine = {}
    for heading, cell in zip(headings, cells):
        textCell = cell.text.strip()
        try:
            linkCell = cell.find('a', href=True)['href']
            dictionnaryCell = {}
            dictionnaryCell['title'] = textCell
            dictionnaryCell['url'] = linkCell
            dictionnaryLine[heading] = dictionnaryCell
        except:
            dictionnaryLine[heading] = textCell
    descriptions.append(dictionnaryLine)

# Json Output
def jsonize(titles, lines):
    tableData = []
    for line in lines:
        dictionary = {}
        for title, cell in zip(titles, line):
            dictionary[title] = cell
        tableData.append(dictionary)
    return tableData

jsonData = jsonize(headings, descriptions)

with open('jsonData.json', 'w') as outfile:
    json.dump(descriptions, fp=outfile, indent=4)
