import matplotlib.pyplot as plt
import string, sys

def read_file(filename: str) -> dict:
    data = {}
    with open(filename) as f:
        while True:
            c = f.read(1).upper()
            if not c: break
            if c in string.ascii_uppercase: data[c] = data.get(c)+1 if data.get(c) is not None else 1
    data = {k:v for k,v in sorted(data.items(), key=lambda item: item[0])}
    return data

filename = sys.argv[1]
freq_of_letters = read_file(filename)

plt.bar(freq_of_letters.keys(), freq_of_letters.values())
plt.title("Frequency Analysis Of Letters")
plt.ylabel("No. of Letters")
plt.show()