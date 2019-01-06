import os
from itertools import cycle

def get_data():
    home_dir = os.path.expanduser('~')
    input_path = f'{home_dir}/code/advent-of-code/problem_2/input.txt'
    data = []
    with open(input_path, 'r') as f:
        for line in f:
            data.append(int(line))

    return data

def find_repeated_frequency(data):
    freqs = set()
    current_freq = 0
    for change in cycle(data):
        freqs.add(current_freq)
        current_freq = current_freq + change

        if current_freq in freqs:
            return current_freq

    return None

if __name__ == "__main__":
    data = get_data()
    print(find_repeated_frequency(data))
