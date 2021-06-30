
with open("text_017.txt", "r") as file:
    words = file.read().lower().split()
    words.sort()
counted = {}
for word in words:
    counted[word] = words.count(word)

for k, v in counted.items():
    print(f'{k} {v}', end=" ")











