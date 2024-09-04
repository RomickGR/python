from abc import abstractmethod


class AddressStrategy:
    @abstractmethod
    def get_address(self, subject, city, street, house_number, floor, flat):
        pass


class ShortAddress(AddressStrategy):
    def get_address(self, subject, city, street, house_number, floor, flat):
        return city + ' ' + street + ' ' + house_number


class FullAddress(AddressStrategy):
    def get_address(self, subject, city, street, house_number, floor, flat):
        return subject + ',' + city + ',' + street + ',' + house_number + ',' + floor + ' этаж' + ',кв №' + flat


class House:
    def __init__(self):
        self.address_strategy = None

    def set_address_strategy(self, address_strategy: AddressStrategy):
        self.address_strategy = address_strategy

    def print_address(self, subject, city, street, house_number, floor, flat):
        print('Result is', self.address_strategy.get_address(subject, city, street, house_number, floor, flat))


if __name__ == "__main__":
    hs = House()
    hs.set_address_strategy(ShortAddress())
    hs.print_address('НСО', 'Новосибирск', 'ул.Ленина', '1', '2', '4')
    hs.set_address_strategy(FullAddress())
    hs.print_address('НСО', 'Новосибирск', 'ул.Ленина', '1', '2', '4')