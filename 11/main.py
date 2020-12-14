
class Solver(object):
    def __init__(self, filename="test.txt"):
        self.filename = filename
        self.rows = self.get_rows(filename)

    def get_rows(self):
        return open(self.filename, "r").read().splitlines()

    def parse_seat(self, seat, seat_idx, row_idx):
        empty = "L"
        occupied = "#"
        floor = "."
        # TODO wez sie za to
        pass

    def iterate_rows(self):
        for row_idx, row in enumerate(self.rows):
            for seat_idx, seat in enumerate(row):
                self.parse_seat(seat, seat_idx, row_idx)
