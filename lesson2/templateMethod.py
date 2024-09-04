from abc import ABC, abstractmethod


class AbstractTransportClass(ABC):
    def start_drive(self) -> None:
        self.start_engine()
        self.push_clutch()
        self.select_gear()
        self.release_the_clutch()
        self.press_accelerator()

    def start_engine(self) -> None:
        print("Запуск двигателя")

    def press_accelerator(self) -> None:
        print("Нажимаем на газ :-)")

    @abstractmethod
    def select_gear(self) -> None:
        pass

    def push_clutch(self) -> None:
        pass

    def release_the_clutch(self) -> None:
        pass


class CarWithMechanicTransmissionClass(AbstractTransportClass):
    def push_clutch(self) -> None:
        print("Нажимаем сцепление")

    def release_the_clutch(self) -> None:
        print("Отпускаем сцепление")

    def select_gear(self) -> None:
        print("Выбрана 1 передача")


class CarWithAutomaticTransmissionClass(AbstractTransportClass):
    def select_gear(self) -> None:
        print("Выбрано положение селектора передач D")


def drive_car(abstract_transport_class: AbstractTransportClass) -> None:
    abstract_transport_class.start_drive()


if __name__ == "__main__":
    print("Сначала едем на механике:")
    drive_car(CarWithMechanicTransmissionClass())

    print("")

    print("Теперь на автомате:")
    drive_car(CarWithAutomaticTransmissionClass())