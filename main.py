import sys
from GWScraper.scraper import GWScraper

def display_help():
    print("GWScraper 0.4.1")
    print("")
    print("Usage: ")
    print("")
    print("   -j   export a json file")
    print("   -c   export a csv file")

arguments_count = len(sys.argv)
if arguments_count == 2:
    first_argument = sys.argv[1]
    ds = GWScraper()

    if first_argument == "-j":
        ds.getJsonData()
    elif first_argument == "-c":
        ds.getCSVData()
    else:
        display_help()
else:
    display_help()