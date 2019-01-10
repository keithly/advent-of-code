import pathlib

def get_data():
    input_path = pathlib.Path(__file__).resolve().parent / 'input.txt'
    return [line.strip() for line in input_path.open()]


def find_common_letters(data):
    for box_1 in data:
        for box_2 in data:
            common_letters = ''
            for letter_1, letter_2 in zip(box_1, box_2):
                if letter_1 == letter_2:
                    common_letters += letter_1
            if len(common_letters) == len(box_1) - 1:
                print(box_1)
                print(box_2)
                return common_letters


if __name__ == "__main__":
    test_data = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
    print(find_common_letters(get_data()))
