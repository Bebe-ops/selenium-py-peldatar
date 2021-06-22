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
