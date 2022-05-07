from urllib.request import urlopen
import json
import pandas as pd

json_url = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
response = urlopen(json_url)
json_data = json.loads(response.read())

def creatingDataframe():
    df = pd.json_normalize(json_data)

    return df

def saveDfAsCsv(df):
    df.to_csv('meteorite_data.csv', sep=';', encoding='utf-8-sig', index=False)

def main():
    df = creatingDataframe()
    saveDfAsCsv(df)

main()