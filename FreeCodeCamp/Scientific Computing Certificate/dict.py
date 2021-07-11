counts = {}

line = input("Enter a line of text: ")

words = line.split()

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts: ', counts)

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])