import csv
import os
from typing import Dict
from pathlib import Path

path_to_write = f'projects.csv'


def is_file_exist(fpath):
    file = Path(fpath)
    return file.is_file() and file.stat().st_size > 0


def csv_writer(data: Dict[str, str]):
    # print(type(data))
    with open(path_to_write, 'a', newline='', encoding='utf-8') as csvfile:
        csv_columns = ['project_name', 'DOI', 'status', 'collection_date', 'publication_date',
                       'LiDAR - Terrestrial', 'Photogrammetry - Terrestrial', 'Photogrammetry - Aerial']

        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        if not is_file_exist(path_to_write):
            writer.writeheader()
        writer.writerow(data)


def csv_reader() -> csv.DictReader:
    with open(path_to_write, 'a', newline='', encoding='utf-8') as csvfile:
        csv_columns = ['project_name', 'DOI', 'status', 'collection_date', 'publication_date',
                       'LiDAR - Terrestrial', 'Photogrammetry - Terrestrial', 'Photogrammetry - Aerial']

        reader = csv.DictReader(csvfile, fieldnames=csv_columns)
        print(type(reader))
        return reader


if __name__ == '__main__':
    from test import parse_single_project

    csv_writer(parse_single_project('https://openheritage3d.org/project.php?id=ws0a-3g91'))
    csv_reader()
