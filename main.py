import sys
import logging
from csv_tools import csv_writer
from openheritage_parser import parse_single_project, parse_data_page
from codetiming import Timer

Timer = Timer()
OPENHERITAGE_DATA_HTML = 'https://openheritage3d.org/data'

data = parse_data_page(OPENHERITAGE_DATA_HTML)

root = logging.getLogger()
root.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)

Timer.start()
for n, i in enumerate(range(len(data))):
    try:
        csv_writer(parse_single_project(data[i]))
    except AttributeError as e:
        print(f'Exception {e} in url {data[i]}')

    formatter = logging.Formatter(f'%(asctime)s - {n+1}/{len(data)} - {data[i]} - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

Timer.stop()
