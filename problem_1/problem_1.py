import os

def sum_lines():
    home_dir = os.path.expanduser('~')
    input_path = f'{home_dir}/code/advent-of-code/problem_1/input.txt'
    total = 0
    with open(input_path, 'r') as f:
        for line in f:
            total = total + int(line)

    return total


if __name__ == "__main__":
    print(sum_lines())
