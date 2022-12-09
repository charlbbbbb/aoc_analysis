import time
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


def get_data(year):
    url = f"https://adventofcode.com/{year}/stats"
    site = requests.get(url)
    soup = bs(site.content, 'html.parser')

    raw_data = soup.find('pre', class_="stats").text

    with open(f"Data Collection/aoc_stats_data/raw_data_{year}.txt", 'x') as data_file:
        data_file.write(raw_data)
        data_file.close()


def convert_to_df(file_path):
    data_frame = {'Day': [],
                  'Part1': [],
                  'Part2': [],
                  'Year': []}
    file = open(file_path, 'r')
    raw_data = file.readlines()
    file.close()
    for line in range(len(raw_data)):
        # noinspection PyTypeChecker
        raw_data[line] = raw_data[line].split()[:-1]

    for day in raw_data:
        try:
            day, part1, part2 = day
            year = file_path.split('_')[-1].replace('.txt', '')

            data_frame['Day'].append(day)
            data_frame['Part1'].append(int(part1))
            data_frame['Part2'].append(int(part2))
            data_frame['Year'].append(year)
        # IF DATA ISN'T AVAILABLE FOR THIS DAY
        except ValueError:
            break

    return pd.DataFrame(data_frame)


def download_all_data(delay):
    years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
    all_dfs = []
    for year in years:
        get_data(year)
        all_dfs.append(convert_to_df(f"Data Collection/aoc_stats_data/raw_data_{year}.txt"))
        time.sleep(delay)


def convert_to_excel():
    years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
    all_dfs = []
    for year in years:
        all_dfs.append(convert_to_df(f"Data Collection/aoc_stats_data/raw_data_{year}.txt"))
    all_years = pd.concat(all_dfs)
    all_years.to_excel('aoc_star_data.xlsx', index=False)


if __name__ == '__main__':
    option = input("Choose an option:\n1: Download all data\n2: Convert all stored data to excel\n")
    if option == '1':
        download_all_data(15)
    elif option == '2':
        convert_to_excel()
    else:
        print("Invalid Option")




