import json
import requests
from bs4 import BeautifulSoup
import os,re


def google_sector_report():
    summ_dic = dict()
    with open('Google Finance.html', 'r') as f:
        response = BeautifulSoup(f, 'lxml')
        main_page = response.find('div', {'id': 'secperf'})
        name22 = [sum.get_text() for sum in main_page.find_all('a')][0:3]
        values22 = [sum.get_text() for sum in main_page.find_all('span', {'class': 'chr'})][0:3]


    with open('Industrials.html') as e:
        response = BeautifulSoup(e, 'lxml')
        main_page = response.find('table', {'id': 'main'})
        name = [sum.get_text() for sum in main_page.find_all('a')][8:]
        values = [sum.get_text().strip('\n') for sum in main_page.find_all('td', {'class': 'selected1'})]
        name3 = name[::len(name) - 1]
        values3 = values[::len(values) - 1]
        # dic1 = {'equity': name[0], 'change': values[0]}
        # dic2 = {'equity': name[-1], 'change': values[-1]}
        # dic_gainer1 = {'result': {f'{name1[0]}': {"biggest_gainer": f"{dic1}", "biggest_loser": f"{dic2}"}}}

    with open('Basic Materials.html') as e:
        response = BeautifulSoup(e, 'lxml')
        main_page = response.find('table', {'id': 'main'})
        name = [sum.get_text() for sum in main_page.find_all('a')][8:]
        values = [sum.get_text().strip('\n') for sum in main_page.find_all('td', {'class': 'selected1'})]
        name2 = name[::len(name) - 1]
        values2 = values[::len(values) - 1]
        # dic1 = {'equity': name[0], 'change': values[0]}
        # dic2 = {'equity': name[-1], 'change': values[-1]}
        # dic_gainer2 = {'result': {f'{name1[0]}': {"biggest_gainer": f"{dic1}", "biggest_loser": f"{dic2}"}}}
        # return dic_gainer2

    with open('Energy.html') as e:
        response = BeautifulSoup(e, 'lxml')
        main_page = response.find('table', {'id': 'main'})
        name = [sum.get_text() for sum in main_page.find_all('a')][8:]
        values = [sum.get_text().strip('\n') for sum in main_page.find_all('td', {'class': 'selected1'})]
        name1 = name[::len(name) - 1]
        values1 = values[::len(values) - 1]
        # dic1 = {'equity': name[0], 'change': values[0]}
        # dic2 = {'equity': name[-1], 'change': values[-1]}
        # dic_gainer3 = {'result': {f'{name1[0]}': {"biggest_gainer": f"{dic1}", "biggest_loser": f"{dic2}"}}}
        # return dic_gainer3

        # summ_dic['result'] = {{name22[0]:{{'biggest_gainer':{'equity':name1[0],'change':values1[0]}},{{'biggest_loser':{'equity':name1[1],'change':values1[1]}}}}} }
    summ_dic['result'] = {name22[0]:[
    {'biggest_gainer':{'equity':name1[0],'change':values1[0]}},
    {'biggest_loser':{'equity':name1[1],'change':values1[1]}},
    {'change':values22[0]}],
    name22[1]:[
    {'biggest_gainer':{'equity':name2[0],'change':values2[0]}},
    {'biggest_loser':{'equity':name2[1],'change':values2[1]}},
    {'change':values22[0]}
    ],
    name22[2]:[
    {'biggest_gainer':{'equity':name3[0],'change':values3[0]}},
    {'biggest_loser':{'equity':name3[1],'change':values3[1]}},
    {'change':values22[0]}
    ]

     }
    x=json.dumps(summ_dic)
    print(x)



google_sector_report()
