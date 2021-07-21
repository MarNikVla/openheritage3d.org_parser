"""
    Module contain functions for sync parsing pages of vacancy from hh.ru
"""
import re
from typing import List

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
def parse_data_page(url: str) -> List[str]:
    list_of_projects_urls = []
    text = session.get(url).text
    soup = BeautifulSoup(text, 'html.parser')
    projects_list = soup.find_all(href=re.compile("project.php"))

    print(len(projects_list))
    print((projects_list[0]))
    for project in projects_list:
        list_of_projects_urls.append(OPENHERITAGE_HTML + '/' + project.get('href'))
    return list_of_projects_urls


def parse_single_project(url: str) -> dict[str: str]:
    project_dict = dict()
    text = session.get(url).text
    soup = BeautifulSoup(text, 'html.parser')

    project_dict['project_name'] = soup.find_all('table')[0].find(
        string='Project Name').find_parent(
        'td').find_next_sibling('td').text
    project_dict['DOI'] = soup.find_all('table')[0].find(string='DOI').find_parent(
        'td').a.get('href').lstrip()
    project_dict['status'] = soup.find_all('table')[0].find(string='Status').find_parent(
        'td').find_next_sibling('td').text


    # project_dict['collection_date'] = soup.find_all('table')[4].text[:len('Background ')]
    table_background = soup.find(
        lambda tag: tag.name == 'table' and 'Background' in tag.text)

    project_dict['collection_date'] = table_background.find(
        string='Collection Date').find_parent('td').find_next_sibling('td').text

    project_dict['publication_date'] = table_background.find(string='Publication Date').find_parent(
        'td').find_next_sibling('td').text

    # print(type(project_dict['project_name']))
    # print(project_dict)

    # add Data Types to project_dict
    table_datatype = soup.find(
        lambda tag: tag.name == 'table' and 'Device Name' in tag.text)
    data_types = table_datatype.find_all('tr')
    for item in data_types:
        key = item.td.text
        value = item.td.find_next_sibling('td').text
        project_dict.update(((key, value),))

    # print(type(project_dict['collection_date']))
    # print(project_dict['status'])
    # print(project_dict['publication_date'])
    # print(table_datatype)
    return project_dict


if __name__ == '__main__':
    parse_single_project('https://openheritage3d.org/project.php?id=ws0a-3g91')
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
