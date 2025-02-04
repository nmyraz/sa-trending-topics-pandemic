import pandas as pd
import numpy as np
import re
import csv
import time

if __name__ == "__main__":

    #set filename for input and output
    fileName = "dataset-5"
    input = f"{fileName}.csv"
    output = f"{fileName}-content.csv"

    # Read csv file into a pandas dataframe
    df = pd.read_csv(f'experiment-dataset/dataset/{input}')

    # Take a look at the first few rows
    print(df.head())


    
    def cleanText(data):
        data = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", " ", data)

        return data

    with open (f'experiment-dataset/dataset/content/{output}', "w") as file:
        writer = csv.writer(file)
        writer.writerow(["content"])

        for index, row in df.iterrows():
            writer.writerow([cleanText(row["content"])])    