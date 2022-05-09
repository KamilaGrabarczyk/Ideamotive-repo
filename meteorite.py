from urllib.request import urlopen
import json
import pandas as pd
import numpy as np

JSON_URL = 'https://data.nasa.gov/resource/gh4g-9sfh.json'


def get_raw_json_data():
    response = urlopen(JSON_URL)
    return json.loads(response.read())


def create_df_from_json(json_data):
    df = pd.json_normalize(json_data).apply(lambda x: x.str.replace('.', ',', regex=False))
    df['year'] = df['year'].str.split('-', 1).str[0]
    df = df[pd.to_numeric(df['year']) >= 1800]
    df['geolocation'] = df['geolocation.latitude'].str.replace(',', '.') + ', ' + df['geolocation.longitude'].str.replace(',', '.')
    return df


def year_criteria(df, start_year, end_year):
    group_year = pd.to_numeric(df['year']).between(start_year, end_year)
    return group_year


def group_year(df):
    criteria = [year_criteria(df, 1800, 1819),
                year_criteria(df, 1820, 1839),
                year_criteria(df, 1840, 1859),
                year_criteria(df, 1860, 1879),
                year_criteria(df, 1880, 1899),
                year_criteria(df, 1900, 1919),
                year_criteria(df, 1920, 1939),
                year_criteria(df, 1940, 1959),
                year_criteria(df, 1960, 1979),
                year_criteria(df, 1980, 1999),
                year_criteria(df, 2000, 9999)]
    values = ["1800-1819",
              "1820-1839",
              "1840-1859",
              "1860-1879",
              "1880-1899",
              "1900-1919",
              "1920-1939",
              "1940-1959",
              "1960-1979",
              "1980-1999",
              "powyżej 2000"]
    grouped_year = np.select(criteria, values, None)
    return grouped_year


def save_df_to_csv(df):
    df.to_csv('meteorite_data.csv', sep=';', encoding='utf-8-sig', index=False)


def main():
    data = get_raw_json_data()
    df = create_df_from_json(data)
    df['grouped_year'] = group_year(df)
    save_df_to_csv(df)


main()
