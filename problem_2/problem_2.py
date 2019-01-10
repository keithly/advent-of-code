import pathlib
from itertools import cycle

def get_data():
    input_path = pathlib.Path(__file__).resolve().parent / 'input.txt'
    return [int(line) for line in input_path.open()]

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
