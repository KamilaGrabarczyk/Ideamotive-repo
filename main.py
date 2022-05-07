from urllib.request import urlopen
import json
import pandas as pd

json_url = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
response = urlopen(json_url)

json_data = json.loads(response.read())


df = pd.read_json(json_url)


data_fields = ['name','id','nametype','recclass','mass','fall','year','reclat','reclong','latitude','longitude']
df = pd.DataFrame(columns=data_fields)
data_list = {key: [] for key in data_fields}

def parseData(val):
    if val == 'latitude' or val == 'longitude':
        target = i['geolocation'][val]

    else:
        target = i[val]

    return target

def fillData():
    for field in data_fields:
        try:
            data_list[field].append(parseData(field))
        except KeyError:
            data_list[field].append("")

        # df[field] = pd.DataFrame(data_list[field])

for i in json_data:
    fillData()




def main():
    jsonToDictData()
    dictDataToDf()
    dfToCsv()

def jsonToDictData():
    for data in json_data:
        for field in data_fields:

        fillData()
def dictDataToDf():
    for field in data_fields:
        df[field] = pd.DataFrame(data_list[field])


def dfToCsv():
    df.to_csv('meteorite_data.csv', sep=';', encoding='utf-8-sig')