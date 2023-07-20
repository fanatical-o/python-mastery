#!/usr/bin/env python3

# compute the sum of the second column multiplied by the third column.

total_cost = 0.0

with open('Data/portfolio.dat', 'r') as f:
    for line in f:
        fields = line.split()
        num_of_shares = int(fields[1])
        #print(num_of_shares)
        share_price = float(fields[2])
        #print(share_price)
        total_cost = total_cost + num_of_shares * share_price

print(total_cost)

