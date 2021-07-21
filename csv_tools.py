import csv
import functools
import itertools
import shutil
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

@functools.lru_cache(maxsize=32)
def csv_to_list():
    list_of_proj_from_csv = list()
    with open(path_to_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=csv_columns)
        for row in reader:
            list_of_proj_from_csv.append((row['project_name'], row['status']))
        return list_of_proj_from_csv


def csv_compare(dict_from_url):
    list_of_proj_from_csv = csv_to_list()
    with open(path_to_file, 'r') as csvfile, open('output.csv', 'w') as outputfile:
        reader = csv.DictReader(csvfile, fieldnames=csv_columns)
        writer = csv.DictWriter(outputfile, fieldnames=csv_columns)


        if (dict_from_url['project_name'], dict_from_url['status']) in list_of_proj_from_csv:
            print('ffff')
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            if not is_file_exist(outputfile):
                writer.writeheader()
            writer.writerow(dict_from_url)
        print(list_of_proj_from_csv)
                # writer.writerow({'first_name': row['first_name'], 'number': row['number']})
    # shutil.move('output.csv', 'names.csv')


# with open('names.csv', 'r') as csvfile, open('output.csv', 'w') as outputfile:
#     reader = csv.DictReader(csvfile, fieldnames=fieldnames)
#     writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
#     for row in reader:
#         if not name == row['first_name']:
#             writer.writerow({'first_name': row['first_name'], 'number': row['number']})
# shutil.move('output.csv','names.csv')

if __name__ == '__main__':
    from openheritage_parser import parse_single_project

    # csv_writer(parse_single_project('https://openheritage3d.org/project.php?id=n3kf-7713'))
    # csv_compare(parse_single_project('https://openheritage3d.org/project.php?id=05r8-we91'))
