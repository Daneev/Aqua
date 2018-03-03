from devices.performance_object import Klapan, Pompa
import time





if __name__ == '__main__':
    print('start')
    klapan = Klapan(5, 3)
    print(klapan.add(2, 3))
    pomp = Pompa(4, 5)
    pomp.on
    klapan.on
    print(pomp.state)
    for t in range(10):
        print("Time is %s" % time.ctime())
        time.sleep(0.7)
    print(pomp.state)
    print(pomp)
    pomp.on
    print(pomp.state)
    for t in range(10):
        print("Time is %s" % time.ctime())
        time.sleep(0.7)
    print(pomp.state)
