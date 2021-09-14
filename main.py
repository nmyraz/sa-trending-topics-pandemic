import json

if __name__ == "__main__":
    # Open file with scraped data
    scrapedData = open("ismail-sabri-vs-remy-ishak.json")

    # Parse scraped data to Dict using json.load()
    parsedScrapedData = json.load(scrapedData)

    # Iterate through the parsed data to input in csv
    for data in parsedScrapedData:
        print(data)