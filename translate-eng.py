import pandas as pd
import numpy as np
import re
import csv
import time
from googletrans import Translator

if __name__ == "__main__":

    #set filename for input and output
    fileName = "umno-19-20"
    input = f"{fileName}.csv"
    output = f"{fileName}-cleaned.csv"

    # Read csv file into a pandas dataframe
    df = pd.read_csv(f'scraped-dataset-csv/{input}')

    # Take a look at the first few rows
    print(df.head())

    # translate data into english
    def transText(data):
        translator = Translator()
        
        time.sleep(0.35)
        result = translator.translate(data, dest='en')
        print(f"Translated {data} to {result.text.lower()}")
        
        # Return a translated text in lowercase
        return result.text.lower()


    with open ("twint-master/dataset-selangor-translated.csv", "w") as file:
        writer = csv.writer(file)
        # bagi nama column untuk buffer file tersebut
        writer.writerow(["tweet"])

    for index, row in df.iterrows():
        writer.writerow([transText(row["tweet"])])