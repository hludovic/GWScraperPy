from requests import get
from bs4 import BeautifulSoup
import json
from datetime import datetime
from db import activities


class Scraper:
    def __init__(self) -> None:
        self.url = "https://wiki.guildwars.com/wiki/Daily_activities"

    def _getHeadings(self, tableData):
        headings = []
        for th in tableData[0].find_all('th'):
            headings.append(th.text.strip())
        return headings

    def _getTableData(self):
        soup = BeautifulSoup(get(self.url).content, 'html.parser')
        return soup.body.table.tbody.find_all('tr') # type: ignore

    def _dateExtractor(self, date: str):
        date_elements = date.split()
        if (len(date_elements) != 3):
            raise Exception("Error date")

        month = 0
        if date_elements[1].lower() == "january":
            month = 1
        elif date_elements[1].lower() == "february":
            month = 2
        elif date_elements[1].lower() == "march":
            month = 3
        elif date_elements[1].lower() == "april":
            month = 4
        elif date_elements[1].lower() == "may":
            month = 5
        elif date_elements[1].lower() == "june":
            month = 6
        elif date_elements[1].lower() == "july":
            month = 7
        elif date_elements[1].lower() == "august":
            month = 8
        elif date_elements[1].lower() == "september":
            month = 9
        elif date_elements[1].lower() == "october":
            month = 10
        elif date_elements[1].lower() == "november":
            month = 11
        elif date_elements[1].lower() == "december":
            month = 12
        else:
            raise IndexError("The monthe of date can't be allowed")
        day = int(date_elements[0])
        year = int(date_elements[2])
        return datetime(year=year, month=month, day=day)

    def _scrapData(self):
        descriptions = []
        tableData = self._getTableData()
        headings = self._getHeadings(tableData)
        tableData.pop(0)
        for line in tableData:
            cells = line.find_all('td')
            dictionnaryLine = {}
            for heading, cell in zip(headings, cells):
                heading = heading.lower().replace(" ", "_")
                textCell = cell.text.strip()
                try:
                    linkCell = cell.find('a', href=True)['href']
                    dictionnaryCell = {}
                    dictionnaryCell['title'] = textCell
                    dictionnaryCell['url'] = linkCell
                    dictionnaryLine[heading] = dictionnaryCell
                except Exception:
                    dictionnaryLine[heading] = self._dateExtractor(textCell).isoformat()  # noqa: E501
            descriptions.append(dictionnaryLine)
        return descriptions

    def getJsonData(self):
        lines = self._scrapData()
        with open('jsonData.json', 'w') as outfile:
            json.dump(lines, fp=outfile, indent=4)

    def updateDatabase(self):
        elements = self._scrapData()
        for element in elements:
            date = element["date"]
            activities[date] = element
