import requests
import csv
from datetime import datetime, timedelta
from google.cloud import storage

def write_blob_from_list(list, bucket, folder, ds_nodash):
    client = storage.Client()
    gcs_bucket = client.get_bucket(bucket)
    path = f"{folder}/{ds_nodash}/ouput.csv"
    blob = gcs_bucket.blob(path)
    with blob.open(mode = 'w') as file:
        writer = csv.writer(file, delimiter = ',')
        for elem in list:
            writer.writerow(elem)

    print(f"Writing {len(list)} rows to gs://{bucket}/{path}")

def get_pitches(ds, bucket, path):
    dt_date = datetime.strptime(ds, '%Y-%m-%d')
    season = dt_date.year
    url = f"https://baseballsavant.mlb.com/statcast_search/csv?all=true&hfPT=&hfAB=&hfBBT=&hfPR=&hfZ=&stadium=&hfBBL=&hfNewZones=&hfGT=R%7CPO%7CS%7C&hfC=&hfSea={season}%7C&hfSit=&player_type=pitcher&hfOuts=&opponent=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt={ds}&game_date_lt={ds}&team=&position=&hfRO=&home_road=&hfFlag=&metric_1=&hfInn=&min_pitches=0&min_results=0&group_by=name&sort_col=pitches&player_event_sort=h_launch_speed&sort_order=desc&min_abs=0&type=details&"
    payload = requests.get(url)
    lines = (line.decode('utf-8-sig') for line in payload.iter_lines())
    data = []
    for row in csv.reader(lines):
        data.append(row)

    write_blob_from_list(data, bucket, path, dt_date.strftime('%Y%m%d'))
