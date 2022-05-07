from urllib.request import urlopen
import json
import pandas as pd

JSON_URL = 'https://data.nasa.gov/resource/gh4g-9sfh.json'


def get_raw_json_data():
    response = urlopen(JSON_URL)
    return json.loads(response.read())


def create_df_from_json(json_data):
    df = pd.json_normalize(json_data)
    return df


def save_df_to_csv(df):
    df.to_csv('meteorite_data.csv', sep=';', encoding='utf-8-sig', index=False)


def main():
    data = get_raw_json_data()
    df = create_df_from_json(data)
    save_df_to_csv(df)


main()
