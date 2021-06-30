import threading
import random
import time

class Philosopher(threading.Thread):
    running = True

    def __init__(self, index, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.index = index
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

def run(self):

    while(self.running):

        time.sleep(30)
        print (f'Philosopher {self.index} is Hungry')
        self.dine()

Philosopher.run = run


def dine(self):

    fork1, fork2 = self.forkOnLeft, self.forkOnRight

    while self.running:

        fork1.acquire()
        locked = fork2.acquire(False)
        
        if locked:
            break
        fork1.release()
        print(f'Philosopher {self.index} swaps forks')
        fork1 , fork2 = fork2, fork1

    else:
        return
    self.dinning()

    fork2.release()
    fork1.release()

Philosopher.dine = dine

def dining(self):
    print(f'Philosopher {self.index} starts eating')
    time.sleep(30)
    print(f'Philosopher {self.index} finishes eating and leaves to think.')
Philosopher.dining = dining


def main():

    forks = [threading.Semaphore() for i in range(5)]

    philosophers = [Philosopher(i, forks[i%5], forks[(i+1)%5])
            for i in range(5)]

    Philosopher.running = True
    for p in philosophers:
        p.start()

    time.sleep(100)
    Philosopher.running = False
    print("Now we're Fininshing.....")

if __name__ ==  "__main__":
    main()
