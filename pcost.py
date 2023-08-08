#!/usr/bin/env python3

# compute the sum of the second column multiplied by the third column.

def portfolio_cost(input_file):
    total_cost = 0.0
    with open(input_file, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                num_of_shares = int(fields[1])
                share_price = float(fields[2])
                total_cost = total_cost + num_of_shares * share_price
            except ValueError as e:
                print(f"Coulnd't parse {line}", end='')
                print(f"Reason: {e}")
    return total_cost

if __name__ == '__main__':
    print(portfolio_cost('Data/portfolio3.dat'))
