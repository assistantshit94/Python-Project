from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book (shit, fro, to):
        print(f"Ticket is booked in train no: {shit.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train No: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is{randint(222, 5555)}")



t = Train(12399)
t.book("Banglore", "pune")
t.getStatus()
t.getFare("Banglore","pune")