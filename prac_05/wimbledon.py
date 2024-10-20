"""
wimbledon
Estimate: 30 minutes
Actual:   38 minutes
"""

import csv
filename = " wimbledon.csv "

def main():
    champions, countries = get_data(filename)
    display_champions(champions)
    display_countries(countries)

def get_data(filename):
    champions = {}
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            champion = parts[2]
            country = parts[3]
            champions[champion] = champions.get(champion, 0) + 1
            countries.add(country)
        return champions, countries

def display_champions(champions):
    print("Wimbledon Champions: ")
    for champion, count in champions.items():
        print(f"{champion} {count}")

def display_countries(countries):
    sorted_countries = sorted(countries)
    country_abbr = [country[:3].upper() if country else "Unknown" for country in sorted_countries]
    print(f"These {len(country_abbr)} countries have won Wimbledon: {', '.join(country_abbr)}")


main()