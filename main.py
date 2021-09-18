import json
import pandas as pd
from pathlib import Path
import csv

if __name__ == "__main__":
    #set filename for input and output
    fileName = "tolak-intimidasi"
    input = f"{fileName}.json"
    output = f"{fileName}.csv"

    #set path to file
    p = Path(f'scraped-dataset-json/{input}')

    #read json
    with p.open('r', encoding='utf-8') as f:
        data = json.loads(f.read())

    #create dataframe
    df = pd.json_normalize(data)

    df.to_csv(f'scraped-dataset-csv/{output}', index=False, encoding='utf-8')