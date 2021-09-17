import pandas as pd
import numpy as np
import re
import csv
import time

if __name__ == "__main__":

    #set filename for input and output
    fileName = "umno-19-20"
    input = f"{fileName}.csv"
    output = f"{fileName}-cleaned.csv"

    # Read csv file into a pandas dataframe
    df = pd.read_csv(f'scraped-dataset-csv/{input}')

    # Take a look at the first few rows
    print(df.head())

    #df.to_csv(f'cleaned-csv-dataset/{output}', index=False, encoding='utf-8')

    def cleanText(data):
        data = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", " ", data)

        return data

    with open (f'cleaned-csv-dataset/{output}', "w") as file:
        writer = csv.writer(file)
        writer.writerow(["content"])

        for index, row in df.iterrows():
            writer.writerow([cleanText(row["content"])])    