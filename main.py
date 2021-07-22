"""
    Main module (entry point)
    usage: python main.py

"""
import sys
import logging
from csv_tools import csv_writer
from openheritage_parser import parse_single_project, parse_data_page
from codetiming import Timer

# Timer to evaluate execution time
Timer = Timer()

# logging
root = logging.getLogger()
root.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)

Timer.start()
data = parse_data_page()
# writing data to csv
for n, i in enumerate(range(len(data))):
    try:
        csv_writer(parse_single_project(data[i]))
    except AttributeError as e:
        print(f'Exception {e} in url {data[i]}')

    # logging
    formatter = logging.Formatter(f'%(asctime)s - {n + 1}/{len(data)} - {data[i]} - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)


Timer.stop()
