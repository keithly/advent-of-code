import os
from itertools import cycle

def get_data():
    home_dir = os.path.expanduser('~')
    input_path = f'{home_dir}/code/advent-of-code/problem_3/input.txt'
    data = []
    with open(input_path, 'r') as f:
        for line in f:
            data.append(str(line).strip())

    return data

if __name__ == "__main__":
    data = get_data()
    print(data)
