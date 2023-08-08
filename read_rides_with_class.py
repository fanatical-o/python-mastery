#!/usr/bin/env python3

import csv

class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides    

def read_rides_with_class(filename):
    records = []

    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            a_row = Row(route=row[0],
            date=row[1],
            daytype=row[2],
            rides=int(row[3]))
            record = (a_row)
            records.append(record)
    return records


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_with_class('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())

