"""
wimbledon
Estimate: 30 minutes
Actual:   38 minutes
"""
import csv
filename = " wimbledon.csv "

def main():
    champions, countries = get_data(filename)

def get_data(filename):
    champions = {}
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split(',')
            champion = parts[2]
            country = parts[3]
            champions[champion] = champions.get(champion, 0) + 1
            countries.add(country)

    print("Wimbledon Champions: ")
    for champion, count in champions.items():
        print(f"{champion} {count}")


main()