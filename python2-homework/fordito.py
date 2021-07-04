# Python program: amely a felhasználótól pozitív számokat kér be mindaddig, amíg a felhasználó nullát nem ad be!
# A program az összes értéket tárolja egy listában, majd írja ki a képernyőre a lista elemeit fordított sorrendben!

numbers = []


def create_list():
    while True:
        input_number = int(input("Kérek egy számot:"))
        if input_number > 0:
            numbers.append(input_number)
        else:
            break
    numbers.reverse()
    print(numbers)


create_list()
