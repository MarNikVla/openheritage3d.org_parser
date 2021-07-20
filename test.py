"""
    Module contain functions for sync parsing pages of vacancy from hh.ru
"""
import re
from typing import List, Dict, Any

from bs4 import BeautifulSoup
import requests

# establishing session
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
})

OPENHERITAGE_HTML = 'https://openheritage3d.org'
OPENHERITAGE_DATA_HTML = 'https://openheritage3d.org/data'
DOI_ROOT = 'https://doi.org'

# Parse hh.ru html_page to list ['vacancy', 'vacancy_link']
def parse_data_page(url) -> List[str]:
    data = []
    text = session.get(url).text
    soup = BeautifulSoup(text, 'html.parser')
    prolect_list = soup.find_all(href=re.compile("project.php"))

    print(len(prolect_list))
    print((prolect_list[0]))
    for project in prolect_list:
        data.append(OPENHERITAGE_HTML+'/'+project.get('href'))
    return data

# /html/body/section/table[1]/tbody/tr[3]/td[2]/in  /html/body/section/table[1]/tbody/tr[3]
def parse_single_project(url) -> Dict[str]:
    project_dict = dict()
    text = session.get(url).text
    soup = BeautifulSoup(text, 'html.parser')

    project_dict['project_name'] = soup.find_all('table')[0].find_all('tr')[2].find_all('td')[1].text
    project_dict['DOI'] = soup.find_all('table')[0].find_all('tr')[1].find_all('td')[1].a.get('href')
    project_dict['status']= soup.find_all('table')[0].find_all('tr')[4].find_all('td')[1].text
    project_dict['collection_date'] = soup.find_all('table')[5].find_all('tr')[2].find_all('td')[1].text
    project_dict['publication_date'] = soup.find_all('table')[5].find_all('tr')[3].find_all('td')[1].text

    data_types = soup.find_all('table')[4].find_all('tr')
    for item in data_types:
        key = item.td.text
        value = item.td.find_next_sibling('td').text
        project_dict.update(((key, value),))
    print(project_dict)
    # print(data_types[1].td)
    # print(data_types[1].td.text)
    # print(data_types[1].td.find_next_sibling('td').text)
    # print(data_types_dict)
    return project_dict


if __name__ == '__main__':
    parse_single_project('https://openheritage3d.org/project.php?id=5b6m-ap62')
    # parse_data_page(OPENHERITAGE_DATA_HTML)

# def get_last_page(vacancy) -> int:
#     first_page = get_html(vacancy)
#     soup = BeautifulSoup(first_page, 'html.parser')
#     last_page = soup.find_all("a",
#                               {'class': ['bloko-button', 'HH-Pager-Control']})[-2].get_text()
#     return int(last_page)
#
# # Make list of urls of giving vacancy
# def url_of_vacancies_to_list(vacancy: str, amount_pages: int = 3) -> List[str]:
#     if amount_pages:
#         last_page = amount_pages
#     else:
#         last_page = get_last_page(vacancy)
#
#     list_of_urls = list()
#     for page in range(last_page):
#         data = parse_vacancy(vacancy, page)
#         for item in data:
#             list_of_urls.append(item['vacancy_link'])
#
#     return list_of_urls
#
