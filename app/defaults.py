import csv
from collections import defaultdict

from .config import Config


def get_counties_and_wards():
    counties = defaultdict(list)
    with open(Config.SRC_FILE, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            county = row[2].title()
            ward = row[0].title()
            counties[county].append(ward)

    return counties
