import pandas as pd
import numpy as np
import re
import csv
import time
from googletrans import Translator

if __name__ == "__main__":

    #set filename for input and output
    fileName = "dataset-3"
    input = f"{fileName}.csv"
    output = f"{fileName}-translated.csv"

    # Read csv file into a pandas dataframe
    df = pd.read_csv(f'experiment-dataset/dataset/{input}')

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


    with open (f'experiment-dataset/dataset/content/translated/{output}', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        # bagi nama column untuk buffer file tersebut
        writer.writerow(["content"])

        for index, row in df.iterrows():
            writer.writerow([transText(row["content"])])