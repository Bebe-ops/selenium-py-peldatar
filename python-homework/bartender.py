age = int(input("Hány éves vagy: "))
order = input(" Mit kérsz? sör vagy cola: ")
drink1 = 'sör'
drink2 = 'cola'

if order != drink1 and order != drink2:
    print("Sorry! Csak sör és cola van!")
    exit()
else:
    if age < 18 and order == drink1:
        print("Nem adhatok sört!")
    elif age > 60 and order == drink2:
        print('Hey tatus! felmegy a vérnyomásod!')
    else:
        print(f'Parancsolj, a {order}!')
