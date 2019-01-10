import pathlib

def get_data():
    input_path = pathlib.Path(__file__).resolve().parent / 'input.txt'
    return [line.strip() for line in input_path.open()]



if __name__ == "__main__":
    #data = get_data()
    test_data = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

