import pathlib

def get_data():
    input_path = pathlib.Path(__file__).resolve().parent / 'input.txt'
    return [line.strip() for line in input_path.open()]


def calc_checksum(test_data):
    twos = 0
    threes = 0
    for box in test_data:
        print(box)
        letter_count = {}
        for letter in box:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
            
            if 2 in letter_count.values():
                twos += 1
            if 3 in letter_count.values():
                threes += 1
            print(letter_count)
    
    print(twos, threes)
    return twos * threes


if __name__ == "__main__":
    #print(get_data())
    test_data = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
    print(calc_checksum(test_data))
