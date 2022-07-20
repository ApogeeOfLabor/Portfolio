from time import sleep

class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелёный']

    def __init__(self) -> None:
        pass

    def running(self):
        sleep_time = [7, 2, 5]
        for i, value in enumerate(sleep_time):
            print(TrafficLight.__color[i], end=' ')
            for _ in range(value):
                print('.', end=' ')
                sleep(1)
            print()

if __name__ == '__main__':
    first_child = TrafficLight()
    first_child.running()