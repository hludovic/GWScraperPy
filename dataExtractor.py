from requests import get
from bs4 import BeautifulSoup
import json
import csv

class DataExtractor:
    def __init__(self) -> None:
        self.url = "https://wiki.guildwars.com/wiki/Daily_activities"
    
    def _getHeadings(self, tableData):
        headings = []
        for th in tableData[0].find_all('th'):
            headings.append(th.text.strip())
        return headings

    def _getTableData(self):
        soup = BeautifulSoup(get(self.url).content, 'html.parser')
        return soup.find('table').find('tbody').find_all('tr')

    def _scrapDataForJson(self):
        descriptions = []
        tableData = self._getTableData()
        headings = self._getHeadings(tableData)
        tableData.pop(0)
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
        return descriptions

    def _scrapDataForCSV(self):
        descriptions = []
        tableData = self._getTableData()
        headings = self._getHeadings(tableData)
        tableData.pop(0)

        for cell in tableData:
            description = []
            for td in cell.find_all('td'):
                description.append(td.text.strip())
            descriptions.append(description)
        return (headings, descriptions)


    def getJsonData(self):
        lines = self._scrapDataForJson()
        with open('jsonData.json', 'w') as outfile:
            json.dump(lines, fp=outfile, indent=4)

    def getCSVData(self):
        scrapedData = self._scrapDataForCSV()
        headings = scrapedData[0]
        lines = scrapedData[1]
        with open("cvsData.csv", "w") as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=",")
            writer.writerow(headings)
            for line in lines:
                writer.writerow(line)
