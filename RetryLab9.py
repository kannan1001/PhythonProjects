#  created a program to read a csv file containing airplane passenger information.when given a seat number and letter it should print passenger name


import csv
class Passenger:
    LastName = ""
    FirstName = ""
    SeatNum = 0
    SeatLetter = ""

    def __init__(self, ln, fn, sn, sl):
        self.LastName = ln
        self.FirstName = fn
        self.SeatNum = sn
        self.SeatLetter = sl


class Jet:
    rows = [[]]

    def __init__(self):
        self.rows = [[None for _ in range(10)] for _ in range(40)]

    def reader(self, csvfile):
        for row in csv.reader(open(csvfile)):
            psngr = Passenger(row[0], row[1], int(row[2]), row[3])
            self.rows[psngr.SeatNum][ord(psngr.SeatLetter) - ord('A')] = psngr


    def output(self):
        print("List of passengers in Airline file:")
        for row in self.rows:
            for eachletter in row:
                if (eachletter == None):
                    next
                else:
                    print(eachletter.LastName, eachletter.FirstName, eachletter.SeatNum, eachletter.SeatLetter)

    def search(self):
        seatnum = int(input(" Enter seat number:"))
        seatletter = input("Enter seat letter:")

        for eachletter in self.rows[seatnum]:
            if eachletter == None:
                continue
            if (eachletter.SeatLetter == seatletter):
                print("\n Passenger seated in ", eachletter.LastName, eachletter.FirstName, eachletter.SeatNum,
                      eachletter.SeatLetter)
                break


s = Jet()
s.reader('Airline.csv')
s.output()
s.search()

