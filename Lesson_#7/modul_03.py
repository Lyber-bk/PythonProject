class cell():

    def __init__(self, cell_count):
        self.cell_count = cell_count

    def __add__(self, other):
        return self.cell_count + other.cell_count

    def __sub__(self, other):
        ret_val = self.cell_count - other.cell_count
        return ret_val if ret_val > 0 else 'error'

    def __mul__(self, other):
        return self.cell_count * other.cell_count

    def __truediv__(self, other):
        return self.cell_count // other.cell_count

    def make_order(self, row_cells):
        self.row_cells = row_cells

        return ('*' * self.row_cells + '\n') * (self.cell_count // self.row_cells) + '*' * (
                    self.cell_count % self.row_cells)


c1 = cell(100)
c2 = cell(6)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)

print(c1.make_order(15))