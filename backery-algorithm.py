import threading
import random
import time


class BackeryAlgorithm():

    def __init__(self):

        self.tickets = [0,1,2,3,4]
        entering = [False]*5

def lock(self, *args):

    self.entering[args[0]] = True
    maximum = 0

    for ticket in self.tickets:
        maximum = max(maximum, ticket)

    self.tickets[args[0]] = maximum + 1
    self.entering[args[0]] = False

    for i in range(len(self.tickets)):

        if i != args[0]:

            while self.entering[i]:
                print("Waiting")


            while self.tickets[i] != 0 and (self.tickets[args[0]] > self.tickets[i]or (self.tickets[args[0]]== self.tickets[i] and args[0]) > i):
                print("waiting")

    print(f"critical section used by process{args[0]}")

    self.tickets[args[0]] = 0

BackeryAlgorithm.lock = lock

def main(self):

    t1 = threading.Thread(target = self.lock, args = (0,))
    t2 = threading.Thread(target = self.lock, args = (1,))
    t3 = threading.Thread(target = self.lock, args = (2,))
    t4 = threading.Thread(target = self.lock, args = (3,))
    t5 = threading.Thread(target = self.lock, args = (4,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

BackeryAlgorithm.main = main

if __name__ == "__ main__":
    b = BackeryAlgorithm()
    b.main()


