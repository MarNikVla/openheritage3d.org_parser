from csv_tools import csv_writer
from test import parse_single_project, parse_data_page
from codetiming import Timer

Timer = Timer()
OPENHERITAGE_DATA_HTML = 'https://openheritage3d.org/data'

# csv_writer(parse_single_project('https://openheritage3d.org/project.php?id=5b6m-ap62'))
# csv_writer(parse_single_project('https://openheritage3d.org/project.php?id=ws0a-3g91'))
# print(parse_data_page(OPENHERITAGE_DATA_HTML)[:3])
data = parse_data_page(OPENHERITAGE_DATA_HTML)

Timer.start()
for n,i in enumerate(range(len(data))):
    print(n)
    try:
        csv_writer(parse_single_project(data[i]))
    except AttributeError as e:
        print(f'Exception {e} in url {data[i]}')
Timer.stop()