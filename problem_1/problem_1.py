import pathlib

def sum_lines():
    input_path = pathlib.Path(__file__).resolve().parent / 'input.txt'
    total = 0
    with open(input_path, 'r') as f:
        for line in f:
            total = total + int(line)

    return total


if __name__ == "__main__":
    print(sum_lines())
