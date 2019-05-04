from COAX_TESTS.parser import uah_to_usd, eur_to_usd


def car_not_found(car):
    print('Автомобіль не знайдено')
    price = int(input('Вкажіть ціну автомобіля -'))
    usd_prise = 0
    currency = int(input(
        'Вкажіть тип валюти (1 - USD, 2 - EUR , UAH - 3)'))
    if currency == 2:
        usd_prise = eur_to_usd(price)
        print('ціна автомобіля в доларах = ', eur_to_usd(price))
    elif currency == 3:
        usd_prise = uah_to_usd(price)
        print('ціна автомобіля в доларах = ', uah_to_usd(price))

    with open("car_catalog", "a") as file:
        file.write(f'\n{car} {int(usd_prise)}')


class CarCatalog:

    def find_car(self, car):
        lst = []
        with open("car_catalog", "r") as file:
            for line in file:
                lst += line.split()
            my_dict = dict(zip(lst[::2], lst[1::2]))
            if my_dict.get(car) is None:
                car_not_found(car)
            else:
                print('Ціна автомобіля - ', my_dict.get(car))


c = CarCatalog()
avto = input('Вкажіть назву автомобіля - ')
c.find_car(avto)
