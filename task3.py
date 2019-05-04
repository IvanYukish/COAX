from COAX_TESTS import parser


class CarCatalog:

    def find_car(self, car):
        with open("car_catalog", "r") as file:
            for line in file:
                lst = line.split()
                my_dict = {lst[0]: lst[1] for i in lst}
                if my_dict.get(car) is None:
                    self.car_not_found(car)
                else:
                    print(my_dict.get(car))

    def car_not_found(self, car):
        print('Автомобіль не знайдено')
        price = input('Вкажіть ціну автомобіля -')
        currency = int(input(
            'Вкажіть тип валюти (1 - USD, 2 - EUR , UAH - 3)'))
        print('ціна автомобіля в доларах = ')
        with open("car_catalog", "w") as file:
            file.write(f'{car} {price}')

    def converter(self):
        pass


c = CarCatalog()
avto = input('Вкажіть назву автомобіля - ')
c.find_car(avto)
