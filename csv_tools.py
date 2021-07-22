import csv
from typing import Dict
from pathlib import Path

path_to_file = f'projects.csv'

# Too many columns ((
csv_columns = ['project_name',
               'DOI',
               'status',
               'collection_date',
               'publication_date',
               # possible data types fields below
               'LiDAR - Terrestrial',
               'LiDAR - Aerial',
               'Photogrammetry - Terrestrial',
               'Photogrammetry - Aerial',
               'Photogrammetry',
               'Not available',
               'Data Derivatives',
               'Data Derivatives - DSM/ORTHO',
               'Data Derivatives - 3D photogrammetry',
               'Data Derivatives - 3D Photogrammetry',
               'Data Derivative - 3D Photogrammetry',
               'Photogrammetry . Aerial',
               ]


# checking is file exist (for adding writer.writeheader() only once)
def is_file_exist(fpath):
    file = Path(fpath)
    return file.is_file() and file.stat().st_size > 0


# write (append) single project to csv project_dict
def csv_writer(data: Dict[str, str]):
    with open(path_to_file, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        if not is_file_exist(path_to_file):
            writer.writeheader()
        writer.writerow(data)
