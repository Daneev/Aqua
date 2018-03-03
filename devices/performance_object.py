'''
Итак, здесь будут описаны классы физических устройств
'''

import threading, time, datetime


class Engine():
    '''
    Базовый класс для создания устройств.
    '''

    def __init__(self, pin, time_loop):
        self.state = 'off'
        self.pin = pin
        # self._time = time_loop
        self.tm = Timer_Device(time_loop, self)

    @property
    def on(self):
        return self._start()

    def _start(self):
        self.state = 'on'

        self.tm.start()
        # self._timer = threading.Timer(0, self._clock)
        # self._timer.start()
        print('{} Start is {}'.format(type(self).__name__, time.ctime()))

    @property
    def off(self):
        return self._stop()

    def _stop(self):
        self.state = 'off'
        # self._timer.cancel()
        print('{} Stop is {}'.format(type(self).__name__, time.ctime()))

    def __str__(self):
        return (type(self).__name__)

    def __repr__(self):
        return 'Device {}'.format(type(self).__name__)


class Timer_Device():
    '''
    Таймер для контроля продолжительности работы устройств.
    '''

    def __init__(self, *args):
        # super(Engine, self).__init__()
        self._time = args[0]
        self.device = args[1]

    def start(self):
        self._timer = threading.Timer(0, self._clock)
        self._timer.start()

    def _clock(self):
        time.sleep(self._time)
        self.stop()

    def stop(self):
        self._timer.cancel()
        self.device.off


class Klapan(Engine):
    '''
    У клапана функция перекрывать воду. Нормальное состояние - закрыт.
    Будем использовать индикатор работы клапана и ограничение непрерывной работы - 15 минут,
    после чего тайм-аут на 15 минут.
    Для управления клапаном используем вывод контроллера - pin
    '''

    def add(self, x, y):
        self.x = x
        self.y = y
        return self.x + self.y


class Pompa(Engine):
    pass


class Datchik():
    def __init__(self):
        pass
