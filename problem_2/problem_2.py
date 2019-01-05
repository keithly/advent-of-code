import os

def get_freqs(data, freqs):
        for x, item in enumerate(data):
            freqs.append(freqs[x] + data[x])
            print(freqs[x])

        return freqs

def get_freqs2(data, freqs):
        for d in data:
            for f in freqs:
                freqs.append(f + d)
                print(f)

        return freqs

def find_duplicates(data):
    seen = {}
    dupes = []

    for x in data:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
            seen[x] += 1
    
    return dupes

def freq_counter():
    data = [3, 3, 4, -2, -4]

    freqs = [0]
    dupes = []
    
    #while len(dupes) == 0:
    freqs = get_freqs(data, freqs)
    dupes = find_duplicates(freqs)
    #if len(dupes) == 0:
    #    freqs = freqs[-1:]
    print('f', freqs)
    print('d', dupes)

    freqs = get_freqs(data, freqs[-1:])
    dupes = find_duplicates(freqs)
    print('f', freqs)
    print('d', dupes)
        
if __name__ == "__main__":
    freq_counter()
