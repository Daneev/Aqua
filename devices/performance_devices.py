'''
Итак, здесь будут описаны классы физических устройств
'''

import threading, time, datetime


class Timer_Device():
    '''
    Таймер для контроля продолжительности работы устройств.
    '''

    def __init__(self, *args):
        self._time = args[0]

    def start(self, device):
        self.device = device
        print('timer start')
        self._timer = threading.Timer(0, self._clock)
        self._timer.start()

    def _clock(self):
        time.sleep(self._time)
        self.stop()

    def stop(self):
        device = self.device
        print('timer stop')
        self._timer.cancel()
        device.off


class Engine():
    '''
    Базовый класс для создания устройств.
    '''

    def __init__(self, pin, time_loop):
        self.state = 'off'
        self.pin = pin
        self._time = time_loop
        self._timer = Timer_Device(self._time)

    @property
    def on(self):
        return self._start()

    def _start(self):
        self.state = 'on'
        self._timer.start(self)
        print('{} Start is {}'.format(type(self).__name__, time.ctime()))

    @property
    def off(self):
        return self._stop()

    def _stop(self):
        self.state = 'off'
        print('{} Stop is {}'.format(type(self).__name__, time.ctime()))

    def __str__(self):
        return (type(self).__name__)

    def __repr__(self):
        return 'Device {}, state {}, pin {}, work_time {}'.format(type(self).__name__, self.state, self.pin, self._time)


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
