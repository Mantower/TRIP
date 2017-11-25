import csv
from random import randint


class RandomCity:

    def get_cities(self):
        rand_ints = []
        for x in range(0,10):
            random_int = randint(1,7323)
            if not random_int in rand_ints:
                rand_ints.append(random_int)
        with open('citydata/cities.csv') as cvsfile:
            cvsreader = csv.reader(cvsfile)
            city_rows = [row for idx, row in enumerate(cvsreader) if idx in rand_ints]
        tags = []
        for tag in city_rows:
            tags.append(tag[1])

        return tags
