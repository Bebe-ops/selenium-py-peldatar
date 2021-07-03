# with open("text_017.txt", "r") as file:
#     words = file.read().lower().split()
#     words.sort()
#
#
#
# counted = {}
# for word in words:
#     counted[word] = words.count(word)
#
# for k, v in counted.items():
#     print(f'{k} {v}', end=" ")


with open("text_017.txt", "r") as file:
    text = file.read().lower()
# print(text)
cleared = text.replace(",", "")
cleared = cleared.replace("\"", "")
cleared = cleared.replace(".", "")
cleared = cleared.replace("_", "")
cleared = cleared.replace("-", "")
cleared = cleared.replace("=", "")
# print(cleared)
my_list = cleared.split()
# print(my_list)

counts = {}
for word in my_list:
    counts[word] = counts.get(word, 0) + 1
print(counts)

for k, v in counts.items():
    print(f'{k} {v}', end=" ")









